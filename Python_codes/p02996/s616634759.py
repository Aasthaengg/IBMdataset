n = int(input())
ablist = [tuple(map(int, input().split())) for _ in range(n)]
ablist.sort(key=lambda x: x[1])

now = 0
for a, b in ablist:
    if now + a <= b:
        now += a
    else:
        print("No")
        break
else:
  print("Yes")