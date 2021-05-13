N = int(input())
K = int(input())
x = list(map(int, input().split()))
x.sort()
ans = 0
for i in x:
    if i > abs(K - i):
        ans += 2 * abs(K - i)
    else:
        ans += 2 * i
print(ans)
