
def solve():
    cnt = 0
    for i in range(N):
        if B[i] > A[i]:
            if B[i] - (A[i]+A[i+1]) > 0:
                cnt += A[i] + A[i+1]
                A[i+1] = 0
            else:
                cnt += B[i]
                A[i+1] = A[i]+A[i+1] - B[i]
        else:
            cnt += B[i]
    print(cnt)
#    print(A)
#    print(B)

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    solve()
