n,m,x=map(int,input().split())
a = list(map(int,input().split()))

cnt_lower=0
cnt_higher=0

for i in a:
    if i>x:
        cnt_lower+=1
    elif i<x:
        cnt_higher+=1
    else:
        continue
        
ans = min(cnt_lower, cnt_higher)
print(ans)