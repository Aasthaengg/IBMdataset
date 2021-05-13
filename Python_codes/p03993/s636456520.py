n=int(input())
a=list(map(int,input().split()))

cnt=0
for i in range(n):
    if a[i] >= 0 and a[a[i] - 1] == i + 1:
        cnt+=1
        a[a[i] - 1] = -1
print(cnt)