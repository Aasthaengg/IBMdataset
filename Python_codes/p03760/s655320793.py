s=input()
r=input()
t=''
for i in range(len(r)):
    t+=s[i]+r[i]
if(len(s)>len(r)):
    t+=s[-1]
print(t)
