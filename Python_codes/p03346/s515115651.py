d = {}
N = int(input())
p = [int(input()) for i in range(N)]

for i in range(N):
    if((p[i]-1) in d):
        d[p[i]] = d[p[i]-1] + 1
    else:
        d[p[i]] = 1

print(N-max(d.values()))