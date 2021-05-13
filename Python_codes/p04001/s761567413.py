s=input()
ans=0
for i in range(2**(len(s)-1)):
  i=bin(i)[2:].zfill(len(s)-1)
  a=s[0]
  for j in range(len(s)-1):
    if i[j]=='1':
      a+='+'
    a+=s[j+1]
  ans+=eval(a)
print(ans)