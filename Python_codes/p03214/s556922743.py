n = int(input())
a = list(map(int, input().split()))

sm = sum(a)
diff = 10000
ans = -1
for i, e in enumerate(a):
    diff_now = abs(e * n - sm)
    if diff_now < diff:
        ans = i
        diff = diff_now

print(ans)
