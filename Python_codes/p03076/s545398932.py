import itertools
t=[0]*5
for i in range(5): t[i]=int(input())
t=list(itertools.permutations(t))
ans=10**5
for i in t:
    a=0
    for j in i:
        if a!=0: a+=0 if a%10==0 else 10-(a%10)
        a+=j
    ans=min(ans,a)
print(ans)