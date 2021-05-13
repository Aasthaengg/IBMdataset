h1, m1, h2, m2, k = map(int, input().split())
if m2-k < 0:
    m2 = 60+(m2-k)
    h2 -= 1
else :
    m2 -= k
minute1 = h1*60+m1
minute2 = h2*60+m2
print(minute2-minute1)
