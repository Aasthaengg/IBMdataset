from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

n,k=nii()
s=input()

happy=0
unhappy=0
for i in range(1,n):
  if s[i-1]==s[i]:
    happy+=1
  else:
    unhappy+=1

for i in range(k):
  if unhappy==1:
    happy+=1
    break
  happy+=2
  unhappy-=2

print(min(happy,n-1))