N, = map(int, input().split())
c = 0
for _ in range(N):
    a, b = map(int, input().split())
    if a == b:
        c += 1
    else:
        c = 0
    if c == 3:
        print("Yes")
        break
else:
    print("No")
