import collections
a,b=map(int,input().split())
c=[list(map(int,input().split())) for i in range(a)]
result=[]
for i in range(a):
    n=c[i][1:]
    result+=n
ans=collections.Counter(result)
ans1,ans2=zip(*ans.most_common())
ans2=list(ans2)
print(ans2.count(a))