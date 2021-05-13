n=int(input())
a=list(map(int,input().split()))
ans=[]
x=n
for i in range(n):
    for j in reversed(range(x)):
        if a[j]==j+1:
            k=a.pop(j)
            ans.append(j+1)
            x-=1
            break
if len(a)==0:
    for i in ans[::-1]:
        print(i)
else:
    print(-1)