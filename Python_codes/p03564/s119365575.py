n=int(input())
k=int(input())
cur=1
while n>0:
    if cur+k<=cur*2:
        cur+=k
    else:
        cur*=2
    n-=1
print(cur)
