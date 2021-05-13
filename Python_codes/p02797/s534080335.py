n, k, s = map(int, input().split())
ans = []
if s < 10**9:
    num = s+1
else:
    num = 1
for i in range(n):
    if i < k:
        ans.append(s)
    else:
        ans.append(num)

print(' '.join(map(str, ans)))