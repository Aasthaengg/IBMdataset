N = int(input())

ans = 0
for i in range(N + 1):
    if i * i > N:
        break
    ans = i
print(ans**2)
