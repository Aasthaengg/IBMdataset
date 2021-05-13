# coding: utf-8

n, m, c = map(int, input().split())
total = 0
count = 0
b_point = input().split()
b_table = [int(k) for k in b_point]
for i in range(n):
    total = 0
    a_point = input().split(" ")
    a_table = [int(m) for m in a_point]
    for j in range(m):
        total += b_table[j] * a_table[j]
        if j == m - 1:
            total += c
            if total > 0:
                count += 1
print(count)
