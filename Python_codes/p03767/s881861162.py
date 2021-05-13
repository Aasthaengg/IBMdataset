N = int(input())
a = list(map(int, input().split()))

cnt = 0
a.sort(reverse=True)

for i in range(1, 2*N, 2):
    cnt += a[i]

print(cnt)