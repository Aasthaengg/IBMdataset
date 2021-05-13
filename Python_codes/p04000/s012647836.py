from collections import Counter
h,w,n=map(int,input().split())
ab=[list(map(int,input().split())) for i in range(n)]
d=(-1,0,1)
c=Counter()
for a,b in ab:
    for da in d:
        for db in d:
            aa=a+da
            bb=b+db
            if 2<=aa<=h-1 and 2<=bb<=w-1:
                c[(aa,bb)]+=1
ans=Counter(c.values())
count_0=(h-2)*(w-2)-sum(ans.values())
print(count_0)
for i in range(1,10):
    print(ans[i])