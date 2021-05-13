s=input()
m=1000
for i in range(len(s)-2):
    tmp=s[i:i+3]
    if abs(753-int(tmp))<m:
        m=abs(753-int(tmp))
print(m)