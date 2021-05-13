n = int(input())
a = list(map(int, input().split()))
ave = sum(a) / n
diff = float('inf')
for i in range(n):
    if diff > abs(a[i]-ave):
        diff = abs(a[i]-ave)
        ans = i

print(ans)