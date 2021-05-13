cnt = [0 for i in range(4)]
for i in range(3):
    a, b = map(int, input().split())
    cnt[a - 1] += 1
    cnt[b - 1] += 1
if sorted(cnt) == [1, 1, 2, 2]:
    print("YES")
else:
    print("NO")