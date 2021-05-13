import sys
input = sys.stdin.readline


def main():
    N = int(input())
    s = input().rstrip()
    t = input().rstrip()

    ans = N
    for i in range(N):
        if s[i:] == t[:N-i]:
            break
        else:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
