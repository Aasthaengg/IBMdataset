from itertools import combinations
L,R=map(int,input().split())
ans=L*R%2019
if R-L>=2018:
    print(0)
else:
    for i in combinations(range(L,R+1),2):
        if ans>=i[0]*i[1]%2019:
            ans=i[0]*i[1]%2019
    print(ans)