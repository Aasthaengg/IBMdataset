from collections import defaultdict
H,W,N=map(int,input().split())
ans=[0 for i in range(10)]

data=defaultdict(int)
def check(a,b):
    if a>0 and a<H-1 and b>0 and b<W-1:return True
    else:return False

def count(a,b):
    for i in range(a-2,a+1):
        for j in range(b-2,b+1):
            if check(i,j):
                x=(i,j)
                data[x]+=1
                
for k in range(N):
    a,b=map(int,input().split())
    count(a,b)

for v in data.values():
    ans[v]+=1

ans[0]=(H-2)*(W-2)-sum(ans[1:])
for i in range(10):
    print(ans[i])
    
#http://arc061.contest.atcoder.jp/data/arc/061/editorial.pdf
#https://atcoder.jp/contests/abc045/submissions/4024831
#https://atcoder.jp/contests/abc045/submissions/4017890