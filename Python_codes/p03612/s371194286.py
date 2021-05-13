n = int(input())
p = [int(i) - 1 for i in input().split()]
cnt_swap = 0
for i in range(n - 1):
    if p[i] == i:
        p[i], p[i + 1] = p[i + 1], p[i]
        cnt_swap += 1
print(cnt_swap if p[n - 1] != n - 1 else cnt_swap + 1)