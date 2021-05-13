a,b=map(str,input().split())
n = a+b
N = int(n)
flag = False
for i in range(1000):
  if i * i == N:
    flag = True
if flag:
  print("Yes")
else:
  print("No")