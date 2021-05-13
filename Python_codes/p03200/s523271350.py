import sys

readline = sys.stdin.readline

def main():
    S = list(readline()[:-1])
    cnt = 0
    ans = 0
    for i, s in enumerate(S):
        if s == 'W':
            ans += i - cnt
            cnt += 1
    print(ans)


if __name__ == "__main__":
    main()
