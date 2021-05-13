n, k = map(int, input().split())
s = input() + '#'

num = [0]
for i in range(1, n + 1):
    if s[i - 1] != s[i]:
        num.append(i)

ans, lennum = num[1], len(num)
for i in range((s[0] == '1') + 1, lennum, 2):
    tmp = num[min(i - 1 + 2 * k, lennum - 1)] - num[max(i - 2, 0)]
    ans = max(ans, tmp)
print(ans)
