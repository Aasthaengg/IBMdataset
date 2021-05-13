from collections import Counter
N=int(input())
A=Counter(list(map(int,input().split())))
ans=0
for key,value in A.items():
    if key<value:
        ans+=value-key
    elif key>value:
        ans+=value
print(ans)
