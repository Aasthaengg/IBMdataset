N,M = map(int,(input().split()))
info = [[] for _ in range(N)]
for i in range(M):
    l,r,d = map(int,(input().split()))
    info[l-1].append([r-1,d])
    info[r-1].append([l-1,-d])

people = [-1]*(N)
flag = 0

not_visited = {}
for i in range(N):
    not_visited[i] = True

stack = list(range(N))

while stack:
    now = stack.pop()

    for j in info[now]:
        if not_visited[j[0]]:
            stack.append(j[0])
        
        if people[j[0]] == -1:
            people[j[0]] = people[now] + j[1] 
        else:
            if people[j[0]] != people[now] + j[1]:
                flag = -1

        not_visited[now] = False

if flag != -1:
    print("Yes")
else:
    print("No")