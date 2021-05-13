n=int(input())
d,x=map(int,input().split())
a=[int(input()) for i in range(n)]

total=0
for j in range(n):
    total+=(d-1)//a[j]

print(total+n+x)