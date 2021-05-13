s = list(input())

ans = float('inf')
for i in range(len(s)-2):
    now = sum(t * 10**i for i, t in enumerate(list(map(int, s[i:i+3]))[::-1]))
    ans = min(ans, abs(now - 753))
print(ans)