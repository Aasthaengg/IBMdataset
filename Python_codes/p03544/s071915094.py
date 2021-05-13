a=2
b=1
N=int(input())
for i in range(N):
  a=a+b
  a,b=b,a
print(a)