N=int(input())
A=list(map(int,input().split()))
a=1
for x in A:
  a*=x
b=0
for y in A:
  b+=a//y
print(a/b)