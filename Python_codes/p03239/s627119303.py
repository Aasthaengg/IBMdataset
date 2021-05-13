N, T = map(int, input().split())
c = [0]*N
t = [0]*N
for i in range(N):
    c[i], t[i] = map(int, input().split())
cc = []
for i in range(N):
    if t[i]<=T:
        cc.append(c[i])

if cc == []:
    print('TLE')
    exit()

print(min(cc))