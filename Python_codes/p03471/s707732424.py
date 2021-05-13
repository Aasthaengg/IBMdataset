N, Y = map(int,input().split())
count = 0

for a in range(N + 1):
    for b in range(N + 1):
        c = N - (a + b)
        if isinstance(c, float) or c < 0:
            continue
        if Y == 10000*a + 5000*b + 1000*c:
            print(a,b,c)
            count += 1
            break
    else:
        continue
    break

if count == 0:
    print('-1 -1 -1 ')