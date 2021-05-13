s=[s for s in input()]
k=int(input())
for i,j in enumerate(s):
  if j=='a':continue
  if ord('z')-ord(j)+1<=k:
    s[i]='a'
    k-=ord('z')-ord(j)+1
  if k==0:break
if k>0:s[-1]=chr(k%26+ord(s[-1]))
print(''.join(s))