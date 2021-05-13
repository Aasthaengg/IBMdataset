n = int(input())
ab = [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
  ab[i].append(ab[i][0]+ab[i][1])
ab = sorted(ab,key = lambda x:x[2],reverse = True)
ans = 0
for i in range(n):
  if i %2 == 0:
    ans += ab[i][0]
  else:
    ans -= ab[i][1]
print(ans)