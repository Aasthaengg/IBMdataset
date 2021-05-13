N, X = map(int, input().split())
L = list(map(int, input().split()))
pos = 0
for i, l in enumerate(L, 1):
    pos += l
    if pos > X:
        print(i)
        break
else:
    print(N + 1)
