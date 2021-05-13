N = int(input())
dic = {}

for _ in range(N):
    i = input()
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

M = int(input())

for _ in range(M):
    j = input()
    if j in dic:
        dic[j] -= 1
    else:
        dic[j] = -1

print(max(0, max(dic.values())))