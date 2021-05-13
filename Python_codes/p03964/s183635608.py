n = int(input())
ta = [list(map(int,input().split())) for _ in range(n)]
ans = [ta[0][0],ta[0][1]]
for i in range(1,n):
  if ans[0] / ta[i][0] <= 1 and ans[1] / ta[i][1] <= 1:
    ans[0] = ta[i][0]
    ans[1] = ta[i][1]
  else:
    x = max(-(-ans[0]//ta[i][0]),-(-ans[1]//ta[i][1]))
    ans[0] = ta[i][0]*x
    ans[1] = ta[i][1]*x
print(sum(ans))