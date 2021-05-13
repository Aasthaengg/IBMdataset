N = int(input())
S = str(input())

ans = 0

for i in range(0, 10):
    a = S.find(str(i))
    if a == -1:
        continue
    for j in range(0, 10):
        b = S.find(str(j), a + 1)
        if b == -1:
            continue
        for k in range(0, 10):
            c = S.find(str(k), b + 1)
            if c == -1:
                continue
            ans += 1
print(ans)
