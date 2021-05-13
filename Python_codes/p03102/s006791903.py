n, m, c = map(int, input().split())
b = list(map(int, input().split()))
cnt = 0
for _ in range(n):
    a = list(map(int, input().split()))
    if sum(i*j for i, j in zip(a, b)) + c > 0:
        cnt += 1 
print(cnt)