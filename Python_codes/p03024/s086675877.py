s=input()
a=0
for i in range(len(s)):
    if s[i]=="o":
        a+=1
if a+15-len(s)>=8:
    print('YES')
else:
    print('NO')