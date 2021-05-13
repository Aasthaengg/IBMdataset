N=int(input())
A=[int(input()) for _ in range(N)]
o=False
for a in A:
  if(a%2==1):
    o=True
print("first" if o else "second")