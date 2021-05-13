a,b,c = map(int, input().split())
k = int(input())
m = max(a,b,c)
for _ in range(k):
  m*=2
if max(a,b,c)==a: print(m+b+c)
elif max(a,b,c)==b: print(a+m+c)
else: print(a+b+m)