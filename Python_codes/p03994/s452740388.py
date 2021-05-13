s=list(input())
n=len(s)
k=int(input())
a=[]
for i in range(n):
  if i==n-1:
    s[i]=chr(97+(ord(s[i])-97+k)%26)
    break
  if s[i]=="a":continue
  t=26-(ord(s[i])-97)%26
  if t>k:continue
  k-=min(t,k)
  s[i]=chr(97+(ord(s[i])-97+t)%26)
print("".join(s))