n=int(input())
a=[int(input()) for _ in range(n)]
b=[0]*(n+1)
count=0
w=1
for i in range(n):
    if b[2]:
        print(count)
        exit()
    b[a[w-1]]+=1
    w=a[w-1]
    count+=1
print("-1")