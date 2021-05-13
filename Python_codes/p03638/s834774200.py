import sys
def input(): return sys.stdin.readline().strip()

def main():
    H, W = map(int, input().split())
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * (H * W)
    idx = 0
    for i in range(N):
        cnt = 0
        while cnt < A[i]:
            ans[idx] = i + 1
            cnt += 1
            idx += 1
    for i in range(H):
        if i % 2 == 0:
            print(" ".join(map(str, ans[W * i: W * (i + 1)])))
        else:
            a = ans[W * i: W * (i + 1)]
            a.reverse()
            print(" ".join(map(str, a)))


if __name__ == "__main__":
    main()
