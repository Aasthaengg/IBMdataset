N = int(input())
AA = map(int,input().split())
AAA = list(AA)
ans = sum(AAA)/N
ans1 = 0
avg = abs(AAA[0] - ans)
for i in range(N):
  if avg > abs(AAA[i]-ans):
    ans1 = i
    avg = abs(AAA[i]-ans)
    
print(ans1)