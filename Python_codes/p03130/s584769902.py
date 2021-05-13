lst = [0] * 5
for _ in range(3):
    a, b = map(int, input().split())
    lst[a] += 1
    lst[b] += 1

if lst.count(2) == 2:
    print ('YES')
else:
    print ('NO')

