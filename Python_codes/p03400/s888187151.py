n=int(input())
d,x=map(int,input().split())
cnt = 0
for i in range(n):
    a = int(input())
    p = 1
    while p <= d:
        p +=a
        cnt +=1
print(cnt+x)
