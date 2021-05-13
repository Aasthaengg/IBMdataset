N = int(input())
n = 1
a = 0
while n <= N:
    n *= 2
    if n > N:
        break
    else:
        a += 1
ans = int(n / 2)
print(ans)