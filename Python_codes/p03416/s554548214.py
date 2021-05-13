def check(i):
    i = str(i)
    return i[:2] == i[4:2:-1]

A, B = map(int, input().split())
res = sum(check(i) for i in range(A, B+1))
print(res)