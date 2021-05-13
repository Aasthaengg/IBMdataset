#https://tjkendev.github.io/procon-library/python/string/rolling_hash.html
class RollingHash():
    def __init__(self, s, base, mod):
        self.mod = mod
        self.pw = pw = [1]*(len(s)+1)
 
        l = len(s)
        self.h = h = [0]*(l+1)
 
        v = 0
        for i in range(l):
            h[i+1] = v = (v * base + ord(s[i])) % mod
        v = 1
        for i in range(l):
            pw[i+1] = v = v * base % mod
    def get(self, l, r):
        return (self.h[r] - self.h[l] * self.pw[r-l]) % self.mod
N=int(input())
S=input()
R1=RollingHash(S,37,10**9+7)
R2=RollingHash(S,29,10**9+9)
ans=0
for ln in range(1,N//2+1):
    D=dict()
    for l in range(N-ln+1):
        tmp=(R1.get(l,l+ln),R2.get(l,l+ln))
        if tmp in D:
            if D[tmp]+ln<=l:
                ans=max(ln,ans)
        else:
            D[tmp]=l
print(ans)
