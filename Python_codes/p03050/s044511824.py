from math import sqrt
from math import ceil
from collections import defaultdict
N=int(input())
done=defaultdict(int)
ans=0
#割る数がi 商とあまりがi 
for i in range(1,ceil(sqrt(N))+1):
    if N//i == N%i:
        if done[i]==0:
            ans+=i
            #print(i)
            done[i]=1
    if (N-i)%i==0:
        if done[(N-i)//i]==0 and (N-i)//i>i:
            ans+=(N-i)//i
            #print((N-i)//i)
            done[(N-i)//i]=1
print(ans)
#print(ceil(sqrt(1000000000000)))