n = int(input())
A = list(map(int, input().split()))
e = []
o = []
e_append = e.append
o_append = o.append

for a in A:
    if a % 2 == 0:
        e_append(a)
    else:
        o_append(a)

if len(o) %2 != 0:
    print('NO')
else:
    print('YES')