n=int(input())
a=[int(i) for i in input().split()]
cnt=0
flag=False
for i in range(1,n):
    if a[i]==a[i-1]:
        if flag:
            flag=False
        else:
            cnt+=1
            flag=True
    else:
        flag=False
print(cnt)