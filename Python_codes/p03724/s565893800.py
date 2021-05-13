n, m = map(int, input().split())

cnt = [0] * -~n
for i in range(m):
    a, b = map(int, input().split())
    cnt[a] += 1
    cnt[b] += 1

for u in cnt:
    if u & 1:
        print("NO")
        exit()

print("YES")
