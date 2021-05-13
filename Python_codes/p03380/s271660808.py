n=int(input())
a=list(map(int,input().split()))
a.sort()
ai=a[-1]
aj=a[0]
for j in range(1,n-1):
    if abs(ai/2-a[j]) < abs(ai/2-aj):
        aj=a[j]
print(ai, aj)