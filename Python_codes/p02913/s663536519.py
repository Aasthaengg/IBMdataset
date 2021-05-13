class RollingHash:

    def __init__(self, string, root, mod):
        self.root = root
        self.mod = mod
        self.hs = [0] * (len(string) + 1)
        self.pw = [1] * (len(string) + 1)
        for i in range(len(string)):
            self.hs[i + 1] = (self.hs[i] * self.root + ord(string[i])) % self.mod
            self.pw[i + 1] = self.pw[i] * self.root % self.mod

    def get_hash(self, l, r):
        "get the hash of s[l:r] (0 <= l <= r <= len(s))"
        return (self.hs[r] - self.hs[l] * self.pw[r - l]) % self.mod

    def __getitem__(self, index):
        if isinstance(index, slice):
            return self.get_hash(index.start, index.stop)
        else:
            return 0


RHMOD = (1 << 61) - 1
class RollingHashMOD61:
    """
    MOD == 2 ** 61 - 1
    参考: https://qiita.com/keymoon/items/11fac5627672a6d6a9f6
    """


    def __init__(self, string, root):
        self.root = root
        self.hs = [0] * (len(string) + 1)
        self.pw = [1] * (len(string) + 1)
        for i in range(len(string)):
            tmp = self.hs[i] * self.root + ord(string[i])
            self.hs[i + 1] = (tmp >> 61) + (tmp & RHMOD)
            tmp = self.pw[i] * self.root
            self.pw[i + 1] = (tmp >> 61) + (tmp & RHMOD)

    def get_hash(self, l, r):
        "get the hash of s[l:r] (0 <= l <= r <= len(s))"
        return (self.hs[r] - self.hs[l] * self.pw[r - l]) % RHMOD
        

    def __getitem__(self, index):
        if isinstance(index, slice):
            return self.get_hash(index.start, index.stop)
        else:
            return 0
        
if __name__ == "__main__":
    N = int(input())
    S = input()

    MOD = 2 ** 61 - 1
    root = 10000

    rh = RollingHashMOD61(S, root)

    ok = 0
    ng = N
    while ng - ok > 1:
        mid = (ok + ng) // 2
        hashes = dict()
        flg = False
        for i in range(N - mid + 1):
            hashofsub = rh[i:i+mid]
            if hashofsub in hashes:
                if i >= hashes[hashofsub] + mid:
                    flg = True
                    break
            else:
                hashes[hashofsub] = i
        
        if flg:
            ok = mid
        else:
            ng = mid

    print(ok)
