import itertools
n,m,q=map(int,input().split())
abcd=[tuple(map(int,input().split())) for _ in range(q)]
h=[]
for i in range(1,m+1):
    h.append(i)
ans=0
for j in itertools.combinations_with_replacement(h,n):
    temp=0
    for a,b,c,d in abcd:
        if j[b-1]-j[a-1]==c:
            temp+=d 
    ans=max(ans,temp)
print(ans)