n,m=map(int,input().split())
list1=[]
ans=[]
for i in range(m):
    a,b=input().split()
    list1.append(a)
    list1.append(b)
for i in range(n):
    ans.append(list1.count(str(i+1)))
for i in range(n):
    print(ans[i])
