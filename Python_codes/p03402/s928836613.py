a, b = map(int, raw_input().split())
w, h = 100, 100
grid = [list("#"*(w/2)+"."*(w/2)) for i in range(h)]
d = (w/2-1)/2
for i in range(a-1):
    r = 2*(i / d)
    c = 2*(i % d)
    grid[r][c] = "."
for i in range(b-1):
    r = 2*(i / d)
    c = w-1-2*(i % d)
    grid[r][c] = "#"
print "%d %d" % (w,h)
print "\n".join(map("".join,grid))