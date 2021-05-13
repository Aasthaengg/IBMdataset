n,m = map(int, input().split())
a = list(map(int, input().split()))
s = 0
total = sum(a)
for i in a:
    if total/(4*m) <= i:
        s += 1

if s >= m:
    print('Yes')
else:
    print('No') 