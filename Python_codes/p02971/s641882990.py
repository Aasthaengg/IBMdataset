N = int(input())

l = [int(input()) for i in range(N)]

new_l = sorted(l)

fmax = new_l[N-1]
fmax2 = new_l[N-2]
smax = fmax

for j in reversed(range(N)):
    if not new_l[j] == fmax:
        smax = new_l[j]
        break

if fmax == fmax2:
    for k in range(N):
        print(fmax)
else:
    for m in range(N):
        if l[m] == fmax:
            print(smax)
        else:
            print(fmax)