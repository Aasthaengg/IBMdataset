s=input()
l=len(s)
k=int(input())
z=''
for i in range(l):
  t=123-ord(s[i])
  if s[i]=='a':
    z+='a'
  elif t<=k:
    z+='a'
    k-=t
  else:
    z+=s[i]
v=ord(z[l-1])-97+k
z=z[:l-1]+chr(v%26+97)
print(z)