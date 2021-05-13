def intMap(): return map(int,input().split())

w,h,x,y = intMap()

s = w * h / 2
multi = 0
if (2 * x == w) and (2 * y == h):
    multi = 1

print("{:.10f} {}".format(s,multi))
