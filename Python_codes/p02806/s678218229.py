N=int(input())
a=[list(input().split()) for _ in range(N)]
X=input()
count=0
flag=0
for i in range(N):
    if X==a[i][0]:
        flag=1
    elif flag==1:
        count+=int(a[i][1])
print(count)
