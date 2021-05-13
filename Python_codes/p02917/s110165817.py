
def solve():
    A = [0]*N
#    A[-1] = 10**6
#    A[0] = 10**6
    A[-1] = B[-1]
    A[0] = B[0]
    for i in range(N-2,0,-1):
        A[i] = min(B[i], B[i-1])
#        print(i)
#    print(A)
    print(sum(A))

if __name__ == "__main__":
    N = int(input())
    B = list(map(int, input().split()))
    solve()  
