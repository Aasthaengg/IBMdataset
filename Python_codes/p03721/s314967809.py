n, k = map(int, input().split())
AB = []
for i in range(n):
    a, b = map(int, input().split())
    AB.append((a, b))
AB.sort()
cnt = 0
for a, b in AB:
    cnt += b
    if cnt >= k:
        print(a)
        break
