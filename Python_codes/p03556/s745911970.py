n = int(input())
ans = 1
for i in range(1, 10 ** 5):
    seq = i ** 2
    if seq <= n:
        ans = seq
    else:
        break
print(ans)