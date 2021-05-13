n = int(input())
xmax, ymax = n//4, n//7
ok = False
for x in range(0, xmax+1):
    for y in range(0, ymax+1):
        if n == 4*x + 7*y:
            ok = True
            break
    if ok: break
print("Yes" if ok else "No")
