sch = []
fin = []
total = 0
cnt,time = map(int,input().split())

for i in range(cnt):
    n,t = input().split()
    sch.append([n,int(t)])

while len(sch) > 0:
    if sch[0][1] <= time:
        total += sch[0][1]
        v = sch.pop(0)
        fin.append([v[0],total])
    else:
        total += time
        sch[0][1] -= time
        last = sch.pop(0)
        sch.append(last)

for i in range(len(fin)):
    print("{0} {1}".format(fin[i][0],fin[i][1]))