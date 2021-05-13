from sys import stdin
ans=0
c=0
N = int(input().rstrip())
for i in range(N):
  c=0
  i+=1
  if i%2==1:
    for j in range(i):
      j+=1
      if i%j==0:
        c+=1
  if c==8:
    ans+=1

print(ans)