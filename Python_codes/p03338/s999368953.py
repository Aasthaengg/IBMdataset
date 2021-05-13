n=int(input())
s=list(input())
a=b=0
for i in range(1,n):
  x=s[:i]
  y=s[i:]
  a=len(set(x)&set(y))
  if a>b:
    b=a
print(b)