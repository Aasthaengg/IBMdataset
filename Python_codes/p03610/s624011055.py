s=list(input())

for i in range(len(s)):
  if i%2==1:
    s[i]=''
  
ss=''.join(map(str,s))

print(ss)