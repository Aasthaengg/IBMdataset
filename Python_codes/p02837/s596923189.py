n = int(input())
xy_ls = [0]*n

for i in range(n):
    a = int(input())
    ls = [list(map(int, input().split())) for _ in range(a)]
    xy_ls[i] = ls 

ok_ls = []
for i in range(2**n):
    ok = 1
    people = [0]*n
    for j in range(n):
        if i >> j & 1:
            people[j] = 1
    for j in range(n):
        if people[j] == 1:
            for xy in xy_ls[j]:
                if xy[1] != people[xy[0]-1]:
                    ok = 0
    if ok:
        ok_ls.append(len([i for i in people if i == 1]))

print(max(ok_ls))