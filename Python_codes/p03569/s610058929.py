S=input()
T=S.replace("x","")
if all(s==t for s,t in zip(T,T[::-1])):
    ans=0
    i=0
    j=len(S)-1
    while i<j:
        pi=i
        pj=j
        while i<len(S) and S[i]=="x":
            i+=1
        while j>=0 and S[j]=="x":
            j-=1
        if i>j:
            break
        ans+=abs(i-pi-pj+j)
        i+=1
        j-=1
    print(ans)
else:
    print(-1)