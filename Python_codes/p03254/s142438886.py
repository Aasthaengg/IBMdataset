N, x = map(int, input().split())
a = list(map(int, input().split()))

a = sorted(a)

M = []
cn = 0

for i in range(N):
    x = x - a[i]


    
    if x >= 0 and i != N-1: 
        cn = cn + 1
    elif x < 0:
        print(cn)
        break
    elif i == N-1:
        if x == 0:
            cn = cn + 1
            print(cn)
            break
        else:
            print(cn)
            break