A, B = map(int, input().split())
if B == 1:
    print(0)
    quit()
else:
    i = 1
    while (A - 1) * i + 1 < B:
        i += 1
    print(i)