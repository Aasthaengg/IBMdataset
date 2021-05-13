N = int(input())
*A, = map(int, input().split())
mod = 10**9 + 7

col = [0, 0, 0]
ans = 1
for a in A:
    if a not in col:
        print(0)
        break
    ans = ans * col.count(a) % mod
    col[col.index(a)] += 1
else:
    print(ans)
