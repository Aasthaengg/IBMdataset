a,b,c=map(int,input().split())
mini = 0
m = a % c
if m == 0:
  mini = a/c
else:
  mini = (c-m + a)/c
maxi = 0
M = b % c
if M == 0:
  maxi = b//c
else:
  maxi = (b-M)//c
res = int(maxi) - int(mini) + 1
print(res)