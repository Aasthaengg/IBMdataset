N = int(input())

pos = []
for _ in range(N):
    tmp = tuple(map(int, input().split()))
    pos.append(tmp)

pos.sort()

dic = dict()
for i in range(N):
    for j in range(i+1,N):
        distance = (pos[j][0]-pos[i][0], pos[j][1]-pos[i][1])
        #print(f'{distance=}')
        if distance in dic:
            dic[distance] += 1
        else:
            dic[distance] = 1
if dic :
    max_frenquency = max(dic.values())

    print(N-max_frenquency)
else:
    print(N)