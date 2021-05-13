N = int(input())
sm = 0
for i in range(N):
    m,c = input().split()
    m = float(m)
    if c == 'JPY':
        sm += m
    else:
        sm += m*380000.0
print(sm)




