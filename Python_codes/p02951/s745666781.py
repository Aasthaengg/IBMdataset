A, B, C = map(int, input().split())

res1 = A - B

if res1 <= C:
    trans = res1
else:
    trans = C

print(C - trans)