n = int(input())
A = list(map(int, input().split()))

ans = 999999

for i in range(100):
    x = 0
    for a in A:
        x += (a-i)**2
    ans = min(ans,x)

print(ans)