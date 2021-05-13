import sys
s=input()
k=int(input())
distinct=0
for i in range(len(s)-1):
  if s[i]!=s[i+1]:
    distinct=1
    first=i
    break
if distinct==0:
  print((len(s)*k)//2)
  sys.exit()
for i in range(len(s)-1,0,-1):
  if s[i]!=s[i-1]:
    last=i
    break
ans=(first+1)//2
ans+=((len(s)-last)//2)
count=1
for i in range(first+1,last):
  if s[i]!=s[i+1]:
    ans+=k*(count//2)
    count=1
  else:
    count+=1
if s[0]==s[-1]:
  ans+=((len(s)+first+1-last)//2)*(k-1)
else:
  ans+=((len(s)-last)//2+(first+1)//2)*(k-1)
print(ans)