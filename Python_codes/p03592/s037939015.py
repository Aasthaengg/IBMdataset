n,m,k=map(int,input().split())
cnt=0
flag =0
for i in range(n+1):
    for j in range(m+1):
        cnt = (m*i) - (i*j) + (j*(n-i))
        if cnt == k:
            flag=1
if flag:
    print("Yes")
else:
    print("No")
