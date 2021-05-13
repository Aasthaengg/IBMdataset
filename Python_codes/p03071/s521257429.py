A, B = map(int, input().split())

res = 0
if A > B:
    res += A
    A -= 1
else:
    res += B
    B -= 1

if A > B:
    res += A
    A -= 1
else:
    res += B
    B -= 1

print(res)
