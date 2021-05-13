import math
x=[int(input()) for _ in range(5)]
y=[math.ceil(i/10)*10 for i in x]
ans_m=sum(y)
ans=sum(y)
for i in range(5):
  ans = min(ans, ans_m-y[i]+x[i])
print(ans)