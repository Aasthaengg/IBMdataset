N = int(input())
P = [list(map(int, input().split())) for i in range(N)]
t = [0] * N
x = [0] * N
y = [0] * N
for i in range(N):
    t[i] = P[i][0]
    x[i] = P[i][1]
    y[i] = P[i][2]

can = True

t.insert(0, 0)
x.insert(0, 0)
y.insert(0, 0)

for i in range(N):
    dt = t[i+1] - t[i]
    dist = abs(x[i+1]-x[i]) + abs(y[i+1]-y[i])
    if dt < dist:
        can = False
        break
    if dt%2 == 0 and dist%2 == 0:
        continue
    elif dt%2 == 1 and dist%2 == 1:
        continue
    else:
        can = False
        break

if can == True:
    print('Yes')
elif can == False:
    print('No')