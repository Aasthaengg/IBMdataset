K,S=map(int,input().split())
ans=0

for i in range(K+1) :
    if S-i>2*K :
        continue
    elif S-i<0 :
        break
    elif 0<=S-i<=K :
        ans+=S-i+1
    else :
        ans+=2*K+i-S+1

print(ans) 