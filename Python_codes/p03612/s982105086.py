def solve():
    ans = 0
    N = int(input())
    P = list(map(int, input().split()))
    lis = [0]*N
    for i in range(N):
        if i+1==P[i]:
            if lis[i-1]==0:
                lis[i]=1
    ans = sum(lis)
    return ans
print(solve())
