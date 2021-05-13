from collections import Counter

n=int(input())
alst=list(map(int,input().split()))

cnt=Counter(alst)
c2=0

for v in cnt.values():
    if v==1:
        continue

    n-=v-1
    if v%2==0:
        c2+=1

print(n if c2%2==0 else n-1)
