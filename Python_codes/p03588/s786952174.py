INF = 1001001001

n = int(input())

a_max = -1
b_min = INF
for i in range(n):
    a, b = map(int, input().split())
    if b_min > b:
        a_max = a
        b_min = b

ans = a_max + b_min
print(ans)