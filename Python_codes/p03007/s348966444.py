N = int(input())
a = tuple(sorted(map(int, input().split())))

ans = []
res = 0
m = a[0]  # 最後に引く側
p = a[-1]  # 最後に足す側
for aa in a[1:N - 1]:
    if aa < 0:
        res -= aa
        ans.append((p, aa))
        p -= aa
    else:
        res += aa
        ans.append((m, aa))
        m -= aa
ans.append((p, m))

res += a[-1] - a[0]
print(res)
for aa in ans:
    print(*aa)
