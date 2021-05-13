c11, c12, c13 = map(int, input().split())

for i in range(2):
    c1, c2, c3 = map(int, input().split())
    if (c1-c11) == (c2-c12) and (c2-c12) == (c3-c13):
        c11, c12, c13 = c1, c2, c3
    else:
        print('No')
        exit()
print('Yes')