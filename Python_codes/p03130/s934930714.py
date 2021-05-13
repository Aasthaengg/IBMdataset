town = [0]*4
for i in range(3):
    a, b = map(int, input().split())
    town[a-1] += 1
    town[b-1] += 1

even = 0
for i in range(4):
    if town[i]%2 == 0:
        even += 1

if even == 2:
    print('YES')
else:
    print('NO')