#11208467
t="abcdefghijklmnopqrstuvwxyz"
s=input()
if s==t[::-1]:print(-1);exit()
if len(s)!=26:
  for i in t:
    if i not in s:print(s+i);exit()
i=25
while s[i-1]>s[i]:i-=1
tt=s[i-1]
ss=list(s[i-1:])
ss.sort()
print(s[:i-1]+ss[ss.index(tt)+1])