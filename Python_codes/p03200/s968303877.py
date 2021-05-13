s=input()
num=len(s)

pre, pst=0,0
for i in range(num):
    if s[i]=='B': pre+=i

s=sorted(s,reverse=1)
for i in range(num):
    if s[i]=='B': pst+=i

print(pst - pre)