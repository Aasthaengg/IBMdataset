r=input()
s=input()
t=1
for i in range(3):
    t*=(r[i]==s[2-i])
print(["NO","YES"][t==1])