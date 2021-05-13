n, k = list(map(int, input().split()))
x = list(map(int, input().split()))
ans = 10**9
for i in range(n-k+1):
  if x[i]*x[i+k-1] < 0:
    temp = min(abs(x[i])+abs(2*x[i+k-1]), abs(2*x[i])+abs(x[i+k-1]))
  else:
    temp = max(abs(x[i]), abs(x[i+k-1]))
  #print(temp)
  if temp< ans:
    ans = temp
print(ans)