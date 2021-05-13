from collections import Counter
a=input()
cnt=Counter(a)
n=len(a)
ans=n*(n-1)//2+1

for v in cnt.values():
    ans-=v*(v-1)//2

print(ans)