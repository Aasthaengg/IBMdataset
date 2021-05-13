def solve():
    N = int(input())
    A = list(map(int,input().split()))
    A = [0] + A + [0]

    sm = 0
    for i in range(N+1):
        sm += abs(A[i] - A[i+1])

    ans = []
    for i in range(1,N+1):
        res = sm - (abs(A[i]-A[i-1])+abs(A[i+1]-A[i])) + abs(A[i+1]-A[i-1])
        ans.append(res)

    print(*ans,sep='\n')

if __name__ == '__main__':
    solve()