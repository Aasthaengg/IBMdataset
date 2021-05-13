n = int(input())
k = int(input())
x_li = list(map(int,input().split()))
s = 0
for i in range(n):
  a = abs(k-x_li[i])
  if a < x_li[i]:
    s += a*2
  else:
    s += x_li[i]*2

print(s)