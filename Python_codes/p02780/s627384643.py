n, k = map(int, input().split())
plst = list(map(int, input().split()))
ans_double = k + sum(plst[:k])
total = ans_double
for i in range(n - k):
    total -= plst[i]
    total += plst[i + k]
    ans_double = max(ans_double, total)
print(ans_double / 2)