H,W,A,B=map(int,input().split())
ans=[]
for h in range(H):
    if h<B:
        ans.append("0"*A+"1"*(W-A))
    else:
        ans.append("1"*A+"0"*(W-A))

for a in ans:
    print(a)