import sys
def input(): return sys.stdin.readline().strip()
mod = 10**9+7

def main():
    N = int(input())

    """
    ダメワードは
        ACG, AGC, GAC, AxGC, AGxC (xはワイルドカード)
    なので、後ろ３文字を見ながらdpすればよさげ
    """

    char = ['A', 'C', 'G', 'T']
    NG1 = {"ACG", "AGC", "GAC"}
    NG2 = {"AAGC", "ACGC", "AGGC", "ATGC", "AGAC", "AGCG", "AGGC", "AGTC"}
    key = []
    for x in char:
        for y in char:
            for z in char:
                word = x + y + z
                if word not in NG1:
                    key.append(word)
    
    zeros = [0] * len(key)
    ones = [1] * len(key)
    d = dict(zip(key, ones))
    
    for _ in range(N - 3):
        d2 = dict(zip(key, zeros))
        for word in d:
            x, y, z = list(word)
            for w in char:
                if (y + z + w not in NG1) and (x + y + z + w not in NG2):
                    d2[y + z + w] += d[x + y + z]
                    d2[y + z + w] %= mod
        d = d2
    
    ans = 0
    for word in d:
        ans += d[word]
        ans %= mod
    print(ans)


if __name__ == "__main__":
    main()
