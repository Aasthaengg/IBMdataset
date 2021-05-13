k = int(input())
x = 0
ans = -1
for i in range(10**6+1):
    x = 10*x + 7
    x %= k
    if x == 0:
        ans = i+1
        break
print(ans)
