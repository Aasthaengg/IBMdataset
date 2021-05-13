n, m = map(int, input().split())
c_list = [0]*n
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    c_list[a] += 1
    c_list[b] += 1

ok = True
for c in c_list:
    if c % 2 != 0:
        ok = False
if ok:
    print("YES")
else:
    print("NO")
