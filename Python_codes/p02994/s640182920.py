n, l = map(int, input().split())
num = 200
for i in range(1, n+1):
    if abs(num) >= abs(l+i-1):
        num = abs(l+i-1)
        x = i
cnt = 0
for j in range(1, n+1):
    cnt += j
print((l-1)*(n-1) + cnt - x)