import sys
stdin=sys.stdin

ip=lambda: int(sp())
fp=lambda: float(sp())
lp=lambda:list(map(int,stdin.readline().split()))
sp=lambda:stdin.readline().rstrip()

n=ip()
a=lp()

a.sort()

rui=[0]

for i in range(n):
  rui.append(rui[-1]+a[i])
  
ch=1

rui.sort(reverse=True)

for j in range(n):
  if rui[j]<=rui[j+1]*3:
    ch+=1
  else:
    break
print(ch)