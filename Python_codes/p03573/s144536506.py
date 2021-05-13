s=list(map(int,input().split()))
if s[0]==s[1]:
  a=2
elif s[1]==s[2]:
  a=0
else:
  a=1
print(s[a])