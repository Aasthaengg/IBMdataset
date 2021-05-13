n = int(input())
k = int(input())
x = list(map(int, input().split()))

ans = 0
for i in x:
    if i <= k//2:
        ans += 2*i
    else:
        ans += 2*(k-i)
print(ans)
