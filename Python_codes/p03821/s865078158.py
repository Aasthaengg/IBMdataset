n=int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
ans=0
for i in range(n):
    #print(ab[-i-1][0]+ans,ab[-i-1][1])
    if (ab[-i-1][0]+ans)%ab[-i-1][1]!=0:
        ans+=ab[-i-1][1]-(ab[-i-1][0]+ans)%ab[-i-1][1]
    #print(ans)
print(ans)