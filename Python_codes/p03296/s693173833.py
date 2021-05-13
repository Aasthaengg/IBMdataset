N = int(input())
a = list(input().split())

cnt = 0
for i in range(1, N):
    if a[i] == a[i-1]:
        a[i] = 'x'
        cnt += 1
print(cnt)


