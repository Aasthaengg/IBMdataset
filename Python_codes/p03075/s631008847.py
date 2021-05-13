l = []
for i in range(5):
    l.append(int(input()))
k = int(input())
ok = True
for i in range(5):
    for j in range(5):
        if i == j: continue
        diff = abs(l[i] - l[j])
        if diff > k:
            ok = False
if ok: print('Yay!')
else: print(':(')