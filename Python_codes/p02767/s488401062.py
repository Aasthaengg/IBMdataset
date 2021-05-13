N = int(input())

X = list(map(int,input().split()))

ans = 10000000000000000

for i in range(101):
    tmp = 0
    for x in X:
        tmp += (i-x)**2
    ans = min(ans, tmp)
print(ans)