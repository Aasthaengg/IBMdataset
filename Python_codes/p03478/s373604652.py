n, a, b = map(int, input().split())

ans = 0
for i in range(1, n+1):
    s = str(i)
    tot = 0
    for c in s:
        tot += ord(c) - ord('0')
    if tot >= a and tot <= b:
        ans += i

print(ans)
