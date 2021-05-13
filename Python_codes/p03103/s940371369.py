from math import ceil
def solve():
    ans = 0
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    A.sort()
    for i in range(N):
        if M<=A[i][1]:
            ans += M*A[i][0]
            break
        else:
            ans += A[i][0]*A[i][1]
            M -= A[i][1]
    return ans
print(solve())