i = lambda: map(int, input().split())
c = lambda x: -x*2+1
h, w = i()
l = []
for q in range(h):
    l += list(i())[::c(q%2)]
o = []
for j in range(w*h-1):
    if l[j] % 2:
        a, b = divmod(j, w)
        y, m, n = a+1, a%2, b==w-1
        x = [b+1, w-b][m]
        o += [[y, x, [y, y+1][n], [x+c(m), x][n]]]
        l[j+1] += 1
print(len(o))
for p in o:
    print(*p)