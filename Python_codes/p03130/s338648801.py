cnt = [0] * 4
for i in range(3):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    cnt[a] += 1
    cnt[b] += 1

one = 0
two = 0
for i in range(4):
    if cnt[i] == 1:
        one += 1
    elif cnt[i] == 2:
        two += 1
if one == two and one == 2:
    print("YES")
else:
    print("NO")
