n=int(input())
a=list(map(int,input().split()))
ptn=1
for i in range(len(a)):
    if a[i]%2==0:
        ptn*=2
print(3**n-ptn)
