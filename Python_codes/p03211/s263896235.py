s=input()
res=[]
for i in range(len(s)-2):
    tmp=s[i:i+3]
    if len(tmp)<3:
        continue
    res.append(abs(753-int(tmp)))
print(min(res))