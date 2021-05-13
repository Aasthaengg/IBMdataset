a, b = map(int, input().split())
c = b-a
k = 1
l = 0
ans = -1
for i in range(2, 1000):
    l = k
    k += i
    if k-l == c:
        ans = k-b
        break

print(ans)
