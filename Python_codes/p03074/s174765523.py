n, k = map(int, input().split())
s = input()

i = 0
x = 0

cumulative = [0]

while i < n:
    i0 = i
    x = s[i]
    while i < n and x == s[i]:
        i += 1
    cumulative.append(cumulative[-1] + i - i0)


x = s[0] == '1'
ans = 0
m = len(cumulative)
for i in range(1, m):
    j = i + 2 * k if x else i + 2 * k - 1
    ans = max(ans, cumulative[min(j, m-1)] - cumulative[i-1])
    if m <= j:
        break
    x = not x
print(ans)
