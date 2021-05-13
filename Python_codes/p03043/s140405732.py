from collections import Counter

n,k=list(map(int,input().split()))
enum=0
denom=2**20

for pip in range(1,n+1):
    cnt=0
    score=pip
    while score<k:
        score*=2
        cnt+=1
    
    enum+=2**(20-cnt)

print(enum/denom/n)