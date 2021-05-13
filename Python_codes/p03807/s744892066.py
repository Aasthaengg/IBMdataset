n = int(input())
a = list(map(int, input().split()))

ar = []
for val in a:
    ar.append(val % 2)

if sum(ar) % 2:
    print('NO')
else:
    print('YES')