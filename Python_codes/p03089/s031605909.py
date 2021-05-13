N = int(input())
B = list(map(int, input().split()))

res = []

while len(B) > 0:
    p = -1
    for i, b in enumerate(B[::-1]):
        j = len(B) - i
        if b == j:
            p = j
            break
    if p == -1:
        print(-1)
        exit()
    else:
        res.append(p)
        B.pop(p - 1)

for r in res[::-1]:
    print(r)
