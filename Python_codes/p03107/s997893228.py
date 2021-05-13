s=input()
k=len(s)
a=0
b=0
for i in range(k):
  if s[i]=='0':
    a+=1
  else:
    b+=1
print(min(a,b)*2)