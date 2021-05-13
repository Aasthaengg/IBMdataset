n=int(input())
k=0
j=0
for i in range(n):
    a,b=map(int,input().split())
    if k<a:
        k=a;j=b
print(k+j)