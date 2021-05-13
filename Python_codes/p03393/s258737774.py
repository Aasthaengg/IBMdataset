S=input()
alphabet=[chr(i) for i in range(ord('a'),ord('z')+1)]
if len(S)!=26:
    for x in alphabet: 
        if not(x in set(S)):
            flag=1
            break
    ans=S+x
    print(ans)
else:
    s=ord(S[25])
    j=25
    for i in range(24,-1,-1):
        if s<ord(S[i]):
            j=i
            s=ord(S[i])
        else:
            break

    if j==0:
        print(-1)
    else:
        l=S[j:]
        y=300
        for x in list(map(ord,l)):
            if ord(S[j-1])<x:
                y=min(y,x)
        ans=S[:j-1]+chr(y)
        print(ans)