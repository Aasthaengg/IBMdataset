n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
b=0
for i in range(2*n):
    if i%2==1:
        b+=a[i]
print(b)
