D=int(input())
c=[int(i) for i in input().split()]
s=[]
for d in range(D):
    s.append([int(i) for i in input().split()])

t=[]
for d in range(D):
    t.append(int(input()) - 1)

v = [0]*D
last = [[0 for i in range(26)] for d in range(D)]

for d in range(D):
    if d>=1:
        last[d] = last[d-1][:]
    last[d][t[d]] = d+1

for d in range(D):
    v[d] = s[d][t[d]] - sum([c[i]*(d+1 - last[d][i]) for i in range(26)])

v_sum=0
for d in range(D):
    v_sum+=v[d]
    print(v_sum)