n = int(input())
a = list(map(int, input().split()))

ave = sum(a) / n
ans_i = 0
ans_v = float("inf")
for i in range(n):
    if abs(ans_v - ave) > abs(a[i] - ave):
        ans_i = i
        ans_v = a[i]

print(ans_i)