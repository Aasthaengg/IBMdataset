N = int(input())

ans = 0
for i in range(1,N+1):
    for j in range(6):
        if 10 ** j <= i and i < 10**(j+1):
            if j % 2 == 0:
                ans += 1
                break

print(ans)