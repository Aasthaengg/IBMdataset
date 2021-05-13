a,b,c,d,e = (int(a) for a in input().split())

h = c-a
m = d-b
if m < 0 :
    h = h-1
    m = 60 + m

print(h * 60 + m - e)