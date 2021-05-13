s=input()
t=input()

frag='No'
for i in range(len(s)):
  st=s[-i:]+s[:-i]
  if st==t:
    frag='Yes'
    break

print(frag)