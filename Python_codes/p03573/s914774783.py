A, B, C = map(int, input().split())
tmp = sorted([A, B, C])

if tmp[0] == tmp[1]:
    print(tmp[2])
else:
    print(tmp[0])
