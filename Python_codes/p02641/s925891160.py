x, n = map(int, input().split())
ok = [True for _ in range(102)]
for p in list(map(int, input().split())):
    ok[p] = False
left, right = 0, 0
while ok[x - left] is False:
    left += 1
while ok[x + right] is False:
    right += 1

if left <= right:
    print(x - left)
else:
    print(x + right)
