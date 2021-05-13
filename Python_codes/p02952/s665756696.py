import math
N=int(input())
order=math.floor(math.log10(N))+1
ans=0
for od in range(1,order+1,2):
    if N<10**od:
        ans+=(N-10**(od-1)+1)
        break
    else:
        ans+=9*10**(od-1)
        od+=1
print(ans)