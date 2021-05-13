from sys import stdin

n,m = map(int,input().split())
cities = [list(map(int,stdin.readline().split())) + [i] for i in range(m)]
for i in range(m):
    cities[i][0] -= 1
state = [[] for i in range(n)]
for i in cities:
    state[i[0]].append([i[1],i[2]])
for i in range(n):
    state[i].sort()
ans = []
for i in range(n):
    temp = "0"*(6-len(str(i+1))) + str(i+1)
    for j in range(len(state[i])):
        s = temp + "0"*(6-len(str(j+1))) + str(j+1)
        ans.append([state[i][j][1],s])
ans.sort()
for i in ans:
    print(i[1])