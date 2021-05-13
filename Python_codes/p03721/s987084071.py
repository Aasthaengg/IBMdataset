N,K = [int(i) for i in input().split()]


kaneko = []

for i in range(N):
    a,b = [int(i) for i in input().split()]
    c = [a,b]
    kaneko.append(c)

kaneko = sorted(kaneko)
sum = 0

for i in range(N):
    sum += kaneko[i][1]
    if sum >= K:
        print(kaneko[i][0])
        break