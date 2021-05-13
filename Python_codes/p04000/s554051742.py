from collections import Counter
h,w,n=map(int,input().split())
d={}

for _ in range(n):
    a,b=map(int,input().split())

    for i in range(max(a-2,1),a+1):
        for j in range(max(b-2,1),b+1):
            if h<i+2 or w<j+2:
                continue
            if (i,j) in d:
                d[(i,j)]+=1
            else:
                d[(i,j)]=1
ans=[0]*10
ans[0]=(h-2)*(w-2)
for k,v in d.items():
    ans[v]+=1
    ans[0]-=1

for a in ans:
    print(a)