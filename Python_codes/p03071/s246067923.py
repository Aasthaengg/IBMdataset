A, B = map(int, input().split())
res = 0
for _ in range(2):
    if A >= B:
        res += A
        A -= 1
    else:
        res += B
        B -= 1
print(res)