n = int(input())
a = list(map(int, input().split()))
key = 1
c = 0
for i in range(n):
    if a[i] != key:
        c += 1
    else:
        key += 1
if c == n:
    print('-1')
else:
    print(c)