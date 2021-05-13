s=input()
m=999999999
for i in range(0,len(s)-2):
    k=int(s[i:i+3])
    if abs(k-753)<m:
        m=abs(k-753)
print(m)
