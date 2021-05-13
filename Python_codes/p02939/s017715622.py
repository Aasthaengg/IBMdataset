import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

def main():
    S = input()
    ans = 0
    before = 'A'
    i = 0
    while i < len(S):
        T = S[i]
        while i + 1 < len(S) and T == before:
            i += 1
            T += S[i]
        i += 1
        ans += 1
        if T == before:
            ans -= 1
        before = T
    print(ans)
if __name__ == '__main__':
    main()