N = int(input())
ret = 0
if N <= 105:
    if N == 105:
        print(1)
    else:
        print(0)
    exit()

ans = 1
for i in range(106, N+1):
    ret = 0
    for j in range(1, i+1):
        if i % j == 0:
            ret += 1
    if ret == 8 and i % 2 == 1:
        ans += 1
print(ans)