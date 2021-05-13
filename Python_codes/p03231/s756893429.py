N,M=map(int,input().split())
S=input()
T=input()

from math import*
ans=N*M//gcd(N,M)

i=0
j=0
count_i=0
count_j=0
while i<N and j<M:
    if count_i==count_j:
        if S[i]!=T[j]:
            ans=-1
    if count_i>count_j:
        count_j+=ans//M
        j+=1
    elif count_j>count_i:
        count_i+=ans//N
        i+=1
    else:
        count_i+=ans//N
        count_j+=ans//M
        i+=1
        j+=1

print(ans)