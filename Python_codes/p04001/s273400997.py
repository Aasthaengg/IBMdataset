import itertools
S=input()
lis = list(itertools.product([0,1], repeat=len(S)-1))
ans=0
for li in lis:
    st=0
    x=0
    for i in range(len(S)-1):
        if li[i]==1:
            x += int(S[st:i+1])
            st = i+1
            
    x += int(S[st:])
    
    ans += x         
print(ans)
