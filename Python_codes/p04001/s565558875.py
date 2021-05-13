S=input()
ans=0
for i in range(2**(len(S)-1)):
    a=bin(i)
    b=a[2:]
    while len(b)<len(S)-1:
        b="0"+b
    k=0
    temp=0
    for j in range(len(b)):
        if b[j]==str(1):
            temp+=int(S[k:j+1])
            k=j+1
    if S[k:len(S)]!="":    
        temp+=int(S[k:len(S)])
    ans+=temp
print(ans)
