#!python3

iim = lambda: map(int, input().rstrip().split())

def resolve():
    N = int(input())
    A = list(iim())

    if N == 0:
        print(1 if A[0] == 1 else -1)
        return

    if A[0] > 0:
        print(-1)
        return

    B = [0]*(N+1)
    x = 1
    B[0] = 1
    for i in range(1, N+1):
        B[i] = B[i-1]*2 - A[i]
        if B[i] < 0:
            print(-1)
            return

    A.reverse()
    B.reverse()
    ans = node = 0
    for d, lim in zip(A, B):
        node = min(node, lim)
        node += d
        ans += node

    print(ans)

if __name__ == "__main__":
    resolve()
