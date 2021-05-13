n = int(input())
s = list(input())
left = [0] * n
right = [0] * n
for i in range(n):
    if s[i] == 'W':
        if i == 0:
            left[0] = 1
        else:
            left[i] = left[i-1] + 1
    elif i != 0:
        left[i] = left[i-1]
for i in range(n-1, -1, -1):
    if s[i] == 'E':
        if i == n - 1:
            right[n-1] = 1
        else:
            right[i] = right[i+1] + 1
    elif i != n - 1:
        right[i] = right[i+1]
ans = right[1]
for i in range(1, n-1):
    ans = min(ans, left[i-1] + right[i+1])
ans = min(ans, left[n-2])
print(ans)