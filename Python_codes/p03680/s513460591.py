import sys
def input(): return sys.stdin.readline().strip()


def main():
    N = int(input())
    A = [0] + [int(input()) for _ in range(N)]
    pushed = [False] * (N + 1)
    pushed[0] = True
    now = 1
    cnt = 0
    while now != 2:
        now = A[now]
        cnt += 1
        if pushed[now]:
            print(-1)
            return
        pushed[now] = True
    print(cnt)



if __name__ == "__main__":
    main()
