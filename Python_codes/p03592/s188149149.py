n, m, k = map(int, input().split())
flag = False
for r in range(n+1):
    for c in range(m+1):
        if m*r + n*c - 2*c*r == k:
            flag = True
            break
    if flag:
        break
print('Yes' if flag else 'No')