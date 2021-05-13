import sys
n=int(input())
a=list(map(int,sys.stdin.read().split()))
a.sort()

ptr,res=0,0
while ptr < n:
  cc=a[ptr]
  f=0
  while ptr < n and a[ptr]==cc:
    f+=1
    ptr+=1
  res+=f%2
print(res)
