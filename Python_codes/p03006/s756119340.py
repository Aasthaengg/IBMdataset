N = int(input())
lis = []
for i in range(N):
    lis.append(tuple(map(int, input().split())))
if N == 1:
    print(1)
    exit()

dic = {}
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        val = (lis[i][0]-lis[j][0], lis[i][1]-lis[j][1])
        if val in dic:
            dic[val] += 1
        else:
            dic[val] = 1
#print(dic)
print(N-max(dic.values()))
