import sys
def input(): return sys.stdin.readline().strip()


def main():
    K = int(input())
    N = 50
    print(N)
    x, y = K // N, K % N
    if y == 0:
        ans = [N + x - 1] * N
        print(" ".join(map(str, ans)))
        return
    ans = [N + x] * N
    for _ in range(N - y):
        max_num, max_idx = ans[0], 0
        for i, a in enumerate(ans):
            if max_num < a:
                max_num, max_idx = a, i
        for i in range(N):
            if i == max_idx:
                ans[i] -= N
            else:
                ans[i] += 1
    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()
