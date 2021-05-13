n = int(input())
a = list(map(int, input().split()))

ave = sum(a)/n
ans = -10
diff = 10**10

for i in range(n):
    diff1 = abs(ave - a[i])
    if diff1 < diff:
        diff = diff1
        ans = i

print(ans)