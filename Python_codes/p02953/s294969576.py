n = int(input())
h = list(map(int, input().split()))
ans = 'Yes'
for i in range(n - 1, 0, -1):
    d = h[i - 1] - h[i]
    if d >= 2:
        ans = 'No'
        break
    elif d == 1:
        h[i - 1] -= 1
print(ans)