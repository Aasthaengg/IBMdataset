n, k = map(int, input().split())
cnt = 1
for i in range(n):
    if i == 0:
        cnt *= k
    else:
        cnt *= (k-1)
print(cnt)