n = int(input())
k = int(input())
x = list(map(int, input().split()))

ans = 0
for i in x:
    if i < k - i:
        ans += i
    else:
        ans += k - i

print(2 * ans)