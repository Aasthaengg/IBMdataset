h1,m1,h2,m2,k = map(int,input().split())
hour = (h2 - h1) * 60
minutes = m2 - m1
print(hour + minutes - k)