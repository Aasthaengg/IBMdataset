import sys

class alphabet(): #Trueなら大文字
    def __init__(self, capitalize):
        self.num = dict() #あるアルファベットが最初から何番目か、0-indexed
        self.index = dict() #i番目のアルファベット
        self.abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"\
            ,"o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        if capitalize: 
            for i in range(26): self.abc[i] = self.abc[i].upper()
        for i, a in enumerate(self.abc):
            self.num[a] = i
            self.index[i] = a

def solve():
    S = list(input())
    length = len(S)
    K = int(input())
    changed = 0
    AB = alphabet(False)
    for i, s in enumerate(S):
        aId = AB.num[s]
        if aId == 0: continue
        else:
            toA = 26 - aId
            if K - changed >= toA: 
                S[i] = "a"
                changed += toA
    if K - changed > 0:
        aId = AB.num[S[length - 1]]
        S[length - 1] = AB.index[(aId + K - changed) % 26]
    print("".join(map(str, S)))
    return 0

if __name__ == "__main__":
    solve()