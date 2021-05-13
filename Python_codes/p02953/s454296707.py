n = int(input())
h = [int(i) for i in input().split()]
ans = 'Yes'
for i in range(n - 1, 0, -1):
    if h[i - 1] > h[i]:
        h[i - 1] -= 1
    if h[i - 1] > h[i]:
        ans = 'No'
print(ans)