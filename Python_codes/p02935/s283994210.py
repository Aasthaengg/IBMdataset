# coding: utf-8

def main():
    N = int(input())
    v = list(map(int, input().split()))
    v.sort()
    ans = v[0] / 2 ** (N - 1)
    for i in range(1, N):
        ans += v[i] / 2 ** (N - i)

    print(ans)

if __name__ == "__main__":
    main()
