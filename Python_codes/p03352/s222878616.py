x = int(input())
if x == 1:
    print(1)
    exit()
ans = 0
for n in range(2, x):
    i = 2
    while n ** i <= x:
        ans = max(ans, n ** i)
        i += 1
print(ans)