s=input()
b=len(s)
a=7-b
for i in range(b):
    if s[i]=="o":
        a+=1
if a>=0:
    print('YES')
else:
    print('NO')