a = sorted(list(map(int, input().split())))
ok = False
for i in range(3):
    if a[i] % 2 ==0:
        ok = True
        break
if not ok:
    ans = a[0]*a[1]
print(0 if ok else ans)