import statistics
import itertools

n, a, b = map(int, input().split())
v = sorted(list(map(int, input().split())), reverse=True)
mean = statistics.mean(v[:a])


# 組み合わせ数を数え上げる
def count_table(n):
    c = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(i + 1):
            if j == 0 or j == i:
                c[i][j] = 1
            else:
                c[i][j] = c[i-1][j-1] + c[i-1][j]
    return c


count_v_a = 0
pos_v_a = 0
for i in range(n):
    if v[i] == v[a-1]:
        count_v_a += 1
        if i < a:
            pos_v_a += 1

c = count_table(n)
count = 0
if pos_v_a == a:
    for pos in range(a, b + 1):
        count += c[count_v_a][pos]
else:
    count += c[count_v_a][pos_v_a]

print(mean)
print(count)
