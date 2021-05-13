n = int(input())
s = 0
for i in range(1, n+1):
    s += i
    if s >= n:
        break

k = s-n
ans = []
for j in range(1, i+1):
    if j == k:
        continue
    else:
        ans.append(j)
ans = list(map(str, ans))
print('\n'.join(ans))
