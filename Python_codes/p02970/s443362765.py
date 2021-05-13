N,D=map(int,input().split())
a = 0
block = 2*D+1
a = N /block
b = int(a)
if a-b > 0:
  a = a+1
print(int(a))