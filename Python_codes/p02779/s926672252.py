n = int(input())
a = list(map(int, input().split()))

s = set()
for i in range(len(a)):
    s.add(a[i])

if len(a) == len(s):
    print('YES')
else:
    print('NO')