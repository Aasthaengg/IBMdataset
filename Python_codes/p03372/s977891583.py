N, c = map(int, input().split())
S = [list(map(int, input().split())) for i in range(N)]

sum_ = 0
r = [0]
for x, v in S:
    sum_ += v
    r.append(sum_-x)

sum_ = 0
l = [0]
for x, v in S[::-1]:
    sum_ += v
    l.append(sum_- (c - x))

def right():
    max_ = r[0]
    for i in r:
        if max_ < i:
            max_ = i
        yield max_

def left():
    max_ = l[0]
    for i in l:
        if max_ < i:
            max_ = i
        yield max_


rm = [[0, 0]] + S
lm = S + [[c, c]]

rpath = list(right())
l_candi = [0]*N
for i in range(N):
    l_candi[i] = l[i] + rpath[-(i + 1)] - (c-lm[-(i + 1)][0])
lmax = max(l_candi)

lpath = list(left())
r_candi = [0]*N
for i in range(N):
    r_candi[i] = r[i] + lpath[-(i + 1)] -rm[i][0]
rmax = max(r_candi)

print(max(rmax, lmax))
