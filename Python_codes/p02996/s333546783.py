N = int(input())
BA = []
for _ in range(N):
    a, b = map(int, input().split())
    BA.append((b, a))
BA.sort()
time = 0
is_timeover = False
for i in range(N):
    b, a = BA[i]
    time += a
    if time > b:
        is_timeover = True
        break

if is_timeover:
    print("No")
else:
    print("Yes")