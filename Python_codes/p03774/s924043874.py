n,m = map(int,input().split())

students = [[int(i) for i in input().split()] for _ in range(n)]
checkpoints = [[int(i) for i in input().split()] for _ in range(m)]

d = []
for i in range(n) :
    d.clear()
    ans = 0
    for j in range(m) :
        x = abs(students[i][0]-checkpoints[j][0])+abs(students[i][1]-checkpoints[j][1])
        d.append(x)
    ans = d.index(min(d))+1
    print(ans)