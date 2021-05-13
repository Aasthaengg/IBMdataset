n = int(input())
p = [int(x) for x in input().split()]

cnt = 0
for i in range(n):
    if p[i] == i + 1:
        cnt += 1
        if i != n - 1:
            p[i], p[i+1] = p[i+1], p[i]
else:
    print(cnt)