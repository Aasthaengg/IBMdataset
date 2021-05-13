n = int(input())
a = list(map(int, input().split()))

res = [0] * n
for i in range(n-1, -1, -1):
    res[i] = (a[i] + sum(res[2*i+1:n:i+1])) % 2

print(res.count(1))
for i in range(n):
    if res[i] == 1:
        print(i+1, end=' ')