N = int(input())
X = list(map(int,input().split()))

ans = 10**10
for i in range(101):
    t = 0
    for x in X:
        t += (x-i)**2
    ans = min(ans, t)
print(ans)