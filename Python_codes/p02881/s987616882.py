N = int(input())
ans = N - 1
p = 1
for i in range(2, int((N ** 0.5) + 1)):
    if p % 2 == 1 and i > (N ** 0.5):
        break
    if N % i == 0:
        p = i
        j = N // i
        m = i + j - 2
        if m < ans:
            ans = m
        else:
            continue
    else:
        continue
print(ans)
