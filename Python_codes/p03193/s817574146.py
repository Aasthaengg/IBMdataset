
n,h,w=map(int,input().split())
count=0
for i in range(n):
    a,b=list(map(int,input().split()))
    if a>=h and b>=w:
        count += 1
print(count)