import sys
input = sys.stdin.readline


def main():
    s = input().strip()
    K = int(input())
    ans = ""
    for c in s:
        if c == "a":
            ans += c
        else:
            cost = 26 - (ord(c) - ord("a"))
            if cost <= K:
                K -= cost
                ans += "a"
            else:
                ans += c
    finalletter = ans[-1]
    ans = ans[:-1] + chr(ord("a") + (ord(finalletter) - ord("a") + K) % 26)
    print(ans)

if __name__ == '__main__':
    main()
