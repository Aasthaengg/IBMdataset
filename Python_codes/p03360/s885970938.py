a,b,c=map(int, input().split())
k=int(input())
s=max(a,b,c)
t=s
for i in range(k):
  s*=2
print(a+b+c+s-t)