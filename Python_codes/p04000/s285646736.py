from collections import Counter
q=[]
h,w,n=map(int,input().split())
for i in range(n):
    x,y=map(int,input().split())
    for j in range(3):
        for k in range(3):
            if (x-2+j)<1 or (x-2+j)>h-2 or (y-2+k)<1 or (y-2+k)>w-2:
                0
            else:
                q.append((x-2+j,y-2+k))
c=Counter(q)
ans=[0]*10
while c:
    ans[c.popitem()[1]]+=1
ans[0]=(h-2)*(w-2)-sum(ans[1:])
for i in ans:
    print(i)