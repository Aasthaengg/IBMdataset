h1, m1, h2,m2,k = map(int, input().split())
if h1 > h2:
    h2 +=24
h = h2 - h1
m = m2 - m1
if m < 0:
    m = m + 60
    h = h - 1
time = h*60 + m 
print(time - k)
