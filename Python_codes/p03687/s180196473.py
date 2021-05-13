def calc(s,char):
  cnt=0
  while s.count(char)<len(s):
    t=""
    for i in range(len(s)-1):
      if char in s[i:i+2]:
        t+=char
      else:
        t+="0"
    s=t
    cnt+=1
  return cnt

s=input()
ans=100
for i in range(26):
  char=chr(ord('a')+i)
  ans=min(ans,calc(s,char))
print(ans)