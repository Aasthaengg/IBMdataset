import sys
from copy import deepcopy
def input(): return sys.stdin.readline().strip()

def main():
    N, x = map(int, input().split())
    A = list(map(int, input().split()))
    if x == 0:
        print(sum(A))
        return

    B = deepcopy(A)
    ans1 = 0
    for i in range(1, N):
        ans1 += max(0, (A[i - 1] + A[i]) - x)
        if A[i] + A[i - 1] > x:
            if A[i] < (A[i - 1] + A[i]) - x:
                A[i] = 0
            else:
                A[i] -= (A[i - 1] + A[i]) - x
    ans2 = 0
    for i in range(N - 2, -1, -1):
        ans2 += max(0, (B[i] + B[i + 1]) - x)
        if B[i] + B[i + 1] > x:
            if B[i] < (B[i] + B[i + 1]) - x:
                B[i] = 0
            else:
                B[i] -= (B[i] + B[i + 1]) - x
    ans = min(ans1, ans2)
    print(ans)



if __name__ == "__main__":
    main()
