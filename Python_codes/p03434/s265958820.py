N = int(input())
a = list(map(int, input().split()))
Alice = 0
Bob = 0

a = sorted(a, reverse=True)
for i in range(N):
    if i % 2 ==0:
        Alice += a[i]
    else:
        Bob += a[i]
ans = Alice - Bob
print(ans)