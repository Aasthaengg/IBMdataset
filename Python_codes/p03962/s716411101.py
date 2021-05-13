a, b, c = map(int,input().split())
n=3
if a==b or b==c or c==a:
  n=2
  if a==b and b==c:
    n=1

print(n)  