n=int(input())
l=sorted(list(map(int,input().split())))

cnt=0
for i in range(0,n-1):
    for j in range(i+1,n):
        cnt+=l[i]*l[j]
print(cnt)