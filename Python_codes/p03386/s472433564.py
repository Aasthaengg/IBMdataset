a,b,k=map(int,input().split())
if k>(b-a):
    k=b-a
list1=[i for i in range(a,a+k)]
list1.extend([i for i in range(b-k+1,b+1)])
ans=list(set(list1))
ans.sort()
if a==b:
    ans=[a]
for i in range(len(ans)):
    print(ans[i])