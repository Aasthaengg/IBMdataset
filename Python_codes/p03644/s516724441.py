n = int(input())


ans = 1
for i in range(10**9):
    if 2**i > n:
        ans = 2**(i-1)
        break

print(ans)