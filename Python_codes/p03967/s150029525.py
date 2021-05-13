s=input()
cnt=0
for i in range(len(s)):
    if i%2==1 and s[i]=='g':
        cnt+=1
    elif i%2==1 and s[i]=='p':
        pass
    elif i%2==0 and s[i]=='g':
        pass
    else:
        cnt-=1
print(cnt)
