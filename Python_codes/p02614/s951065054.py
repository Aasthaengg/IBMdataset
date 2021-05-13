#k = int(input())
h, w,k = map(int, input().split())
#al = list(map(int, input().split()))
cl=[list(input()) for i in range(h)]
import itertools
import copy
def countBlack(l):
    res=0
    for li in l:
        res+= li.count('#')
    return res

rows=[0,1]
cols=[0,1]
ans=0
for rowpt in itertools.product(rows,repeat=h):
    for colpt in itertools.product(cols,repeat=w):
        cl_temp=copy.deepcopy(cl)
        # 行を塗る
        for i in range(h):
            if rowpt[i]==1:
                for j in range(w):
                    cl_temp[i][j]='r'
        for j in range(w):
            if colpt[j]==1:
                for i in range(h):
                    cl_temp[i][j]='r'
        if countBlack(cl_temp)==k:
            ans+=1
print(ans)