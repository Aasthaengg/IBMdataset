s=input()
k=int(input())
ans=''
for i in range(len(s)-1):
  if s[i]=='a':
    ans+='a'
  else:
    if k>=123-ord(s[i]):
      k-=(123-ord(s[i]))
      ans+='a'
    else:
      ans+=s[i]
ans+=chr((ord(s[-1])-97+k)%26+97)
print(ans)