from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

s=input()
t=input()

for i in range(len(s)):
  s=s[-1]+s[:-1]
  if s==t:
    print('Yes')
    exit()

print('No')