s=list(input())
K=int(input())
A=[chr(ord('a') + i) for i in range(26)]+[chr(ord('a') + i) for i in range(26)]
for i in range(len(s)):
  a=A.index(s[i])
  if i==len(s)-1:
    K%=26
    s[i]=A[a+K]
    break
  if s[i]=='a':
    continue
  if K>=26-a:
    K-=(26-a)
    s[i]='a'
  else:
    continue
print(*s,sep='')