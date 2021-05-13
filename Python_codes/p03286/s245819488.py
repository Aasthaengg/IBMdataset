n = int(input())
ans = []
d = 0
while n:
    select = n & 1
    ans.append(select)
    if d & 1:
        n += select
    else:
        n -= select
    d += 1
    n >>= 1
if not ans:
    ans.append(0)
print(''.join(map(str, reversed(ans))))
