N = int(input())
ans = 0
if N <= 3:
    print(N)
    exit(0)
for i in range(2, 33):
    for j in range(2, 11):
        t = i ** j
        if t <= N:
            ans = max(ans, t)
print(ans)
