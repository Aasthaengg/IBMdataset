a = []
while True:
    b = map(int, raw_input().split())
    if b == [0, 0]:
        break
    a.append(b)
for list in a:
    n, x = list
    c = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i + j + k == x - 3 and i < j and j < k:
                    c += 1
    print c