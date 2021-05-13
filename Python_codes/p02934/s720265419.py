n=int(input())
a=list(map(int,input().split()))

bunbo=0

for i in range(n):
  b=1/a[i]
  bunbo+=b

print(1/bunbo)