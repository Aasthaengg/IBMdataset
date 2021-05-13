o=input()
s=input()
p=[""]*(len(o)+len(s))
for i in range(len(o)):
  p[i*2]=o[i]
for i in range(len(s)):
  p[i*2+1]=s[i]

print("".join(p))
