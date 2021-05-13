n, t = map(int, input().split())
a = [int(x) for x in input().split()]
lst = [0]
mina = a[0]
for i in range(1, n):
    mina = min(mina, a[i-1])
    lst.append(max(0, a[i]-mina))

lst.sort(reverse=True)
cnt = 1
for i in range(1, n):
    if lst[0] == lst[i]: cnt += 1
    else: break

print(cnt)