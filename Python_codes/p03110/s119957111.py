N = int(input())
xu = []
for i in range(N):
    xu.append(input().split())

answer = 0
for i in range(N):
    if xu[i][1] == 'JPY':
        answer += int(xu[i][0])
    else:
        answer += float(xu[i][0]) * 380000.0
print(answer)