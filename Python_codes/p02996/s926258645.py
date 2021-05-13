N = int(input())
times = []
for i in range(N):
    A, B = map(int, input().split())
    times.append([A, B])

times.sort(key=lambda x:x[1])

t = 0
for i in range(N):
    t += times[i][0]
    if t > times[i][1]:
        print('No')
        exit()

print('Yes')