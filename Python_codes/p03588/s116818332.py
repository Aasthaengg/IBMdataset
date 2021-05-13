N=int(input())
ab=[list(map(int,input().split()))for _ in range(N)]

ab.sort()
ans=ab[-1][0]+ab[-1][1]
print(ans)