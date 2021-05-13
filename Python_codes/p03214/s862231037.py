n = int(input())
a = list(map(int, input().split()))

avg = sum(a) / len(a)
diff = list(map(lambda x : abs(x - avg), a))
min_diff = min(diff)
for i in range(n):
    if abs(a[i] - avg) == min_diff:
        print(i)
        break