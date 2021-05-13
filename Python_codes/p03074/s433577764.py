n, k = map(int, input().split())
s = input().rstrip()

starts = [0]
ends = []

for i in range(1, n-1):
    if s[i] == '1' and s[i-1] == '0':
        starts.append(i)
    if s[i] == '1' and s[i+1] == '0' and len(starts) == len(ends) + 2:
        ends.append(i)

ends.append(n-1)

ans = 0
m = len(ends)
for i in range(m-k+1):
    ans = max(ans, ends[i+k-1] - starts[i] + 1)

if k >= m:
    ans = n

print(ans)