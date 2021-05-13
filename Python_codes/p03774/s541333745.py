N,M = map(int,input().split())
point = []
target = []
ans = []
for i in range(N):
    person = list(map(int,input().split()))
    point.append(person)
for j in range(M):
    goal = list(map(int,input().split()))
    target.append(goal)
for k in point:
    check = []
    for l in target:
        a = 0
        a += abs(k[0]-l[0])+abs(k[1]-l[1])
        check.append(a)
    b = min(check)
    ans.append(check.index(b))
for m in ans:
    print(m+1)