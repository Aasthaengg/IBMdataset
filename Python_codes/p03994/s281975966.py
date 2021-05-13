s=list(input())
K=int(input())
for i in range(len(s)):
    if i==len(s)-1:
        K=K%26
        x=ord(s[i])
        for j in range(K):
            x+=1
            if x==123:
                x=97
        s[i]=chr(x)
    else:
        if K<=0 or s[i]=='a':
            continue
        dif=123-ord(s[i])
        if dif<=K:
            s[i]='a'
            K-=dif
print(''.join(s))