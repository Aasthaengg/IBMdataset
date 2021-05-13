a,b,c = map(int, input().split())
can = False
for i in range(a + 1):
    for j in range(b + 1):
        cnt = i * (b - j) + j * (a - i)
        if cnt == c:
            can = True
print("Yes" if can else "No")