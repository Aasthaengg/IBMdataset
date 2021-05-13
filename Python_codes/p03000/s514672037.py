n, x = map(int, input().split())
L = list(map(int, input().split()))
D = [0]
for i in range(n):
    D += [L[i] + D[i]]
ans = 0
for d in D:
    if d <= x:
        ans += 1
    else:
        break
print(ans)
