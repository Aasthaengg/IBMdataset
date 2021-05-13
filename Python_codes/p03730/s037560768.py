A, B, C = list(map(int, input().split()))
i = 1
d_set = set()
while(True):
    d = A*i % B
    if d == C:
        print('YES')
        break
    if d in d_set:
        print('NO')
        break
    d_set.add(d)
    i += 1