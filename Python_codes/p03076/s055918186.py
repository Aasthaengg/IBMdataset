l = []
for i in range(5): l.append(int(input()))
ok = False
for i in range(5):
    if l[i] % 10 != 0: ok = True
if ok == 0:
    print(sum(l))
    exit()
mini = 9
for i in range(5):
    if l[i] % 10 != 0 and l[i] % 10 < mini % 10:
        mini = l[i]
ans = mini
for i in range(5):
    d = l[i] // 10
    if l[i] % 10 != 0: d += 1
    ans += d * 10
d = mini // 10
d += 1
ans -= d * 10
print(ans)