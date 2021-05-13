def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int,input().split())
        A.append(a)
        B.append(b)
    
    A.sort()
    B.sort(reverse=True)

    if N % 2 == 0:
        tmp = (B[N//2]+B[N//2-1])/2 - (A[N//2]+A[N//2-1])/2
        print(int(tmp / 0.5)+1)
    else:
        print(B[N//2] - A[N//2] + 1)
    
if __name__ == '__main__':
    solve()