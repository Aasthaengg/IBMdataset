h1,m1,h2,m2,k = map(int,input().split())
if m2 < m1:
    m2 += 60
    h2 -= 1
time = (h2 - h1) * 60 + (m2 - m1)

print(time - k)
