N = int(input())

for i in range(1, N+1):
    if i == 1:
        ans = 1
    else:
        ans = ans * i % (10**9 + 7)

print(ans)