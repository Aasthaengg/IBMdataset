A, B = map(int, input().split())
cnt = 0
for i in range(A, B + 1):
    c = str(i)
    if (c[0], c[1]) == (c[-1], c[-2]):
        cnt += 1
print(cnt)
