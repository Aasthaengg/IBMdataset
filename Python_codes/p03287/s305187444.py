#!python3

# input
N, M = list(map(int, input().split()))
A = list(map(int, input().split()))


def main():
    x = 0
    m = {0: 1}
    ans = 0
    for i in range(N):
        x = (x + A[i]) % M
        if x in m:
            ans += m[x]
            m[x] += 1
        else:
            m[x] = 1

    print(ans)


if __name__ == "__main__":
    main()
