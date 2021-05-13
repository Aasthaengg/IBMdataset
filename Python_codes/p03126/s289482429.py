n,m = map(int,input().split())
ans = [int(0) for i in range(m+1)]
for i in range(n):
    k = list(map(int,input().split()))
    for j in range(1,k[0]+1):
        ans[k[j]] += 1
#print(ans)
cnt = 0
for i in range(1,len(ans)):
    if ans[i]==n:
        cnt += 1
print(cnt)