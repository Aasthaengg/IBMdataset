n = int(input())
a = list(map(int,input().split()))
a.sort()
sm = []
sm.append(a[0])
for i in range(1,n):
    sm.append(sm[-1]+a[i])
num = 0
for i in range(1,n):
    if sm[i-1] * 2 < a[i]:
        num = i
        
print(n - num)
