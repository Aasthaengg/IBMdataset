import sys

input = sys.stdin.readline


def main():
    N = int(input())
    s = [0] * N
    for i in range(N):
        s[i] = int(input())

    s.sort()
    ans = sum(s)
    if ans % 10 == 0:
        for i in range(N):
            if s[i] % 10 != 0:
                ans -= s[i]
                break
        if i == N - 1:
            ans = 0
    
    print(ans)


if __name__ == "__main__":
    main()
