N=int(input())
s1=list(input())
s2=list(input())
i=0
beflag=0        #0…前は何もない(先頭)、1…前は横ミノ×2、2…前は縦ミノ×1
ans=1
p=10**9+7
while i<N:
    if s1[i]==s2[i]:        #もし縦ミノなら
        if beflag==0:
            ans=(ans*3)%p
        elif beflag==1:
            ans=ans
        elif beflag==2:
            ans=(ans*2)%p
        beflag=2
        i=i+1
    else:                   #それ以外は横ミノ*2を保証するはず
        if beflag==0:
            ans=(ans*6)%p
        elif beflag==1:
            ans=(ans*3)%p
        elif beflag==2:
            ans=(ans*2)%p
        beflag=1
        i=i+2
    #print(i,ans,N)
print(ans)

