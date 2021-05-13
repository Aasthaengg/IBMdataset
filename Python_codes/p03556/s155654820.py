N = int(input())

ans = 1
for i in range(N):
    if i**2 > N:
        ans = (i-1)**2
        break

print(ans)