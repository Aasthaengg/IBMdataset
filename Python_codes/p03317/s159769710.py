n, k = map(int, input().split())
s = input()
i = s.find("1")/2
ans = 0

# former part
while ans * (k-1) < i:
    ans += 1
i = max(i, ans * (k-1))

# latter part
tmp = 0
while tmp * (k-1) + i < n-1:
    tmp += 1

print(ans + tmp)
