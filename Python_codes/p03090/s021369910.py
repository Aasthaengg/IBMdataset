n = int(input())
if n % 2 == 0:
    a = [(i, n - i + 1) for i in range(1, n // 2 + 1)]
else:
    a = [(i, n - i) for i in range(1, n // 2 + 1)]
    a.append((n,))
ans = []
for i in range(len(a) - 1):
    for a1 in a[i]:
        for a2 in a[i+1]:
            ans.append((a1, a2))
if len(a) > 2:
    for a1 in a[0]:
        for a2 in a[len(a)-1]:
            ans.append((a1, a2))
print(len(ans))
for i in ans:
    print('{} {}'.format(i[0], i[1]))
