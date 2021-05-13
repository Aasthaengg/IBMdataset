n = int(input().strip())
a = list(map(int, input().split()))
reps = []

a.sort()
tmp = 0
for e in a:
    if e == tmp:
        reps.append(e)
        tmp = 0
    else:
        tmp = e
if len(reps) < 2:
    print(0)
else:
    print(reps[-1] * reps[-2])
