from collections import defaultdict


def main():
    H, W, N = map(int, input().split())
    cnt = defaultdict(lambda: defaultdict(lambda: 0))
    ans = [0] * 10
    ans[0] = (H-2)*(W-2)
    for _ in range(N):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        for i in range(a-1, a+2):
            for j in range(b-1, b+2):
                if i < 1 or H-1 <= i or j < 1 or W-1 <= j:
                    continue
                c = cnt[i][j]
                ans[c] -= 1
                ans[c+1] += 1
                cnt[i][j] = c+1
    for a in ans:
        print(a)

if __name__ == "__main__":
    main()
