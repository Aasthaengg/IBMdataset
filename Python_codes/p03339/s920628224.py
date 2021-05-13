N = int(input())
S = list(input())
data = []
data.append((0, 0))
for i in range(N):
    # looking left
    if S[i] == 'W':
        data.append((data[i][0]+1, data[i][1]))
    # looking right
    elif S[i] == 'E':
        data.append((data[i][0], data[i][1]+1))
#print(data)

answer = N-1
for i in range(N):
    count = 0
    count += data[N][1] - data[i+1][1]
    count += data[i][0]
    if answer > count:
        answer = count

print(answer)
