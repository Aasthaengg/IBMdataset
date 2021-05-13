n = int(input())
d, x = map(int, input().split())
a = [int(input()) for _ in range(n)]
c = 0
for k in a:
    if d % k == 0:
        c += d // k
    else:
        c += d // k + 1
print(x + c)