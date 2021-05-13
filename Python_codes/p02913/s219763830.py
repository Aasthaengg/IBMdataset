N=int(input())
S=input()

ans=0

for slide in range(1,N):
    pos=slide
    bpos=0
    while pos<N:
        clen=0
        while pos<N and clen<slide and S[pos]==S[bpos]:
            pos+=1
            bpos+=1
            clen+=1
        
        ans=max(ans,clen)

        if clen==0:
            pos+=1
            bpos+=1

print(ans)
