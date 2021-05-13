N,T = map(int,input().split())
t_l = []
for i in range(N):
    c,t = map(int,input().split())
    if t <= T:
        t_l.append(c)
if t_l == []:
    print('TLE')
else:
    print(min(t_l))