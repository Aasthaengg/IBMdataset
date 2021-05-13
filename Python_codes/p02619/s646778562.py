D = int(input())
c = list(map(int,input().split()))
s = []
for i in range(D):
    s.append(list(map(int,input().split())))
t = [int(input()) for _ in range(D)]
def my_index(l,x,d,default=False):
    if x in l:
        return l.index(x)
    else:
        return d
def last(d,i):
    a= t[:d]
    a.reverse()
    day = -1*(my_index(a,i,d))+d
    return day
score = 0
for d in range(1,D+1):
    score += s[d-1][t[d-1]-1]
    for i in range(1,27):
        score -= c[i-1]*(d-last(d,i))
    print(score)