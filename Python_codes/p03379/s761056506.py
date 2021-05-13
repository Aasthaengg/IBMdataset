n = int(input())
x = list(enumerate(map(int, input().split())))
x.sort(key=lambda x:x[1])
ans = [""]*n
for i in range(n):
  if (n+1)//2 >= i+1: ans[x[i][0]] = x[(n+1)//2][1]
  else: ans[x[i][0]] = x[(n+1)//2-1][1]

print("\n".join(map(str, ans)))