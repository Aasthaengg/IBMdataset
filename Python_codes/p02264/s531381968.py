n,q = map(int, input().split())
name = []
time = []
for i in range(n):
    x = input().split()
    name.append(x[0])
    time.append(int(x[1]))

t = 0
n_end = []
t_end = []
while(len(time) > 0):
    if time[0] <= q:
        t += time[0]
        n_end.append(name.pop(0))
        time.pop(0)
        t_end.append(t)
    else :
        t += q
        time[0] -= q
        a = time.pop(0)
        b = name.pop(0)
        time.append(a)
        name.append(b)

for i in range(len(n_end)):
    print(n_end[i],t_end[i])

