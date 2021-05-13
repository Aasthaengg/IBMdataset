n,k=map(int,input().split())
s=input()

if n==1:
  print(0)
  exit()

happy=0
cnt=0
for i in range(n-1):
  if s[i]==s[i+1]:
    happy+=1
  else:
    cnt+=1

print(min(n-1,happy+min(cnt,k)*2))