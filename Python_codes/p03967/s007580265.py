s=input()
dif=0
for i in range(len(s)):
    if s[i]=='g':
        dif+=1
    else:
        dif-=1
print(dif//2)