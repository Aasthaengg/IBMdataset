import sys
class alphabet: #Trueなら大文字
    def __init__(self, capitalize):
        self.num = dict()
        self.index = dict()
        self.abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"\
            ,"o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        if capitalize: 
            for i in range(26): self.abc[i] = self.abc[i].upper()
        for i, a in enumerate(self.abc):
            self.num[a] = i
            self.index[i] = a

def solve():
    input = sys.stdin.readline
    N = int(input())
    S = input().strip("\n")
    AB = alphabet(False)
    Count = [1] * 26
    for i in range(len(S)):
        Count[AB.num[S[i]]] += 1
    mod = 7 + 10 ** 9
    Ans = 1
    for i, n in enumerate(Count):
        Ans *= n
        Ans %= mod
    print((Ans - 1 + mod) % mod)


    return 0

if __name__ == "__main__":
    solve()