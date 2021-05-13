n = int(input())
A = list(map(int, input().split()))
s = set()

for a in A:
    if a in s:
        print('NO')
        break
    s.add(a)
else:
    print('YES')