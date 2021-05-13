s=input()
n=len(s)
r=0
b=0
for i in s:
    if i=="1":
        r+=1
    else:
        b+=1
print(min(r,b)*2)
