n = int(input())
p = list(map(int, input().split()))
q = [i for i in range(1, n+1)]
cnt = 0
for j in range(n):
    if p[j] == q[j]:
        if j != n-1:
            p[j], p[j+1] = p[j+1], p[j]
            cnt += 1
        else :
            p[j], p[j-1] = p[j-1], p[j]
            cnt += 1
print(cnt)
