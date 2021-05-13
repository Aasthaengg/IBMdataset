n=int(input())
a=[int(i) for i in input().split()]
ans=[]
positive_flag=True


if 0<=min(a):
        positive_flag=True
elif max(a)<=0:
        positive_flag=False
elif min(a)*(-1) <= max(a):
        positive_flag=True
        maxId=a.index(max(a))
        for i in range(n):
                if i!=maxId:
                        ans.append([maxId+1,i+1])
else:
        positive_flag=False
        minId=a.index(min(a))
        for i in range(n):
                if i!=minId:
                        ans.append([minId+1,i+1])

if positive_flag:
        for i in range(1,n):
                ans.append([i,i+1])
else:
        for i in range(n,1,-1):
                ans.append([i,i-1])

print(len(ans))
for num in ans:
        print(str(num[0])+" "+str(num[1]))