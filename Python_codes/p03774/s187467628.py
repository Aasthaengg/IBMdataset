import sys
input = lambda: sys.stdin.readline()
exec("try:sys.stdin=open('input.txt','r');sys.stdout=open('output.txt','w')\nexcept:pass")

n, m = map(int, input().split())
student, point = [], []
for i in range(n):
    student.append(list(map(int, input().split())))
for i in range(m):
    point.append(list(map(int, input().split())))
dist = []
for i in range(n):
    temp = []
    for j in range(m):
        temp.append([j, abs(student[i][0] - point[j][0]) +
                     abs(student[i][1] - point[j][1])])
    dist.append(temp)
# for dis in dist:
#     print(dis)
tot = []
for dis in dist:
    ans = []
    minn = min(dis, key=lambda i: i[1])
    for i in dis:
        if i[1] == minn[1]:
            ans.append(i[0])
    ans.sort()
    print(ans[0] + 1)
# print(tot)
