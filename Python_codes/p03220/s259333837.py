n = int(input())
t,a = map(int,input().split())
h = list(map(int,input().split()))
mi = 1000000000
for i in range(n):
    if mi > abs(a-(t-h[i]*0.006)):
        mi = abs(a-(t-h[i]*0.006))
        ans = i+1
print(ans)
