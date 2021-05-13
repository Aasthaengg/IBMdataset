s="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
t={}
for i in range(26):
  t[s[i]]=i

n=int(input())
ss=input()
r=""
for i in ss:
  r+=s[(t[i]+n)%26]
print(r)