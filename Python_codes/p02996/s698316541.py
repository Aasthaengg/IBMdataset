N = int(input())
Q = []

for i in range(N):
    Q.append(tuple(map(int, input().split())))

Q = sorted(Q, key=lambda x: x[1])
now = 0
for i in range(N):
    if now + Q[i][0] <= Q[i][1]:
        now += Q[i][0]
    else:
        print("No")
        exit()

print("Yes")