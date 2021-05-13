import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    S = input().strip()

    ans = 0
    f = False
    for i, s in enumerate(S):
        if f:
            ans += 9
        elif i == len(S) - 1:
            ans += int(S[i])
        else:
            if S[i + 1] != "9":
                f = True
                ans += int(S[i]) - 1
            else:
                ans += int(S[i])

    print(ans)

    
    

if __name__ == '__main__':
    main()

