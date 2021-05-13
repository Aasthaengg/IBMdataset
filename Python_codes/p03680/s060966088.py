import sys
n=int(input())
a=list(map(int,sys.stdin.read().split()))
check_a=[False for _ in range(n)]
c=0
i=0
while True:
  if i == 1:
    print(c)
    exit()
  nex=a[i]-1
  if check_a[i]:
    break
  check_a[i]=True
  i=nex
  c+=1
print(-1)