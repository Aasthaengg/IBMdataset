n = int(input())
d,x = map(int,input().split())
res = 0
for i in range(n):
  a = int(input())
  for j in range(1,d+1,a):
    res += 1
print(res+x)