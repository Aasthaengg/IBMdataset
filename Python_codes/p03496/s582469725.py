n=int(input())
*l,=map(int,input().split())
a,b=max(l),min(l)
pa,pb=l.index(a),l.index(b)

print(2*n-1)
if abs(a)>=abs(b):
  for i in range(n):
    print(pa+1,i+1)
  for i in range(n-1):
    print(i+1,i+2)
else:
  for i in range(n):
    print(pb+1,i+1)
  for i in range(n-1):
    print(n-i,n-i-1)