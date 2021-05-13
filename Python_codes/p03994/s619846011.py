s=input()
k=int(input())
sl=[]
n=len(s)
for i in range(n):
  if s[i]!='a':
    if 26-(ord(s[i])-97)<=k:
      sl.append('a')
      k-=26-(ord(s[i])-97)
    else:
      sl.append(s[i])
  else:
    sl.append(s[i])
if k>0:
  if k%26!=0:
    sl[n-1]=chr(ord(sl[n-1])+k%26)
print(''.join(sl))