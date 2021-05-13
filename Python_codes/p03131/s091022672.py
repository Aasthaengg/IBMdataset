from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

k,a,b=nii()

num=1
if b-a<=1:
  print(num+k)
  exit()

if num<a:
  k-=a-num
  num+=a-num

cnt=k//2
if k%2==0:
  num+=(b-a)*cnt
else:
  num+=(b-a)*cnt+1

print(num)