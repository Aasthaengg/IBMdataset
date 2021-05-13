s=list(str(input()))
w=int(input())
t=''
for i in range(len(s)):
  if i%w==0:
    t+=s[i]
print(t)