n,m=map(int,input().split())
a=[]
b=[]

cnt=0
k=0
flag=0
for i in range(n):
    a.append(input())
for i in range(m):
    b.append(input())

for j in range(n-m+1):
    k=0
    for i in range(n-m+1):
        if b[k]==a[i][j:j+m]:
            k+=1
            if k==m:
                print("Yes")
                flag+=1
                break
    else:
        continue
    break


if flag==0:
    print("No")

