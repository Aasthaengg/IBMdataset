n=int(input())
a=[list(map(int,input().split())) for i in range(n)][::-1]
b=0
for i in range(n):
    if (b+a[i][0])%a[i][1]==0:
        continue
    b+=a[i][1]-(b+a[i][0])%a[i][1]
print(b)