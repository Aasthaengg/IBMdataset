a = sorted(list(map(int, input().split())))
ok = False
for i in a:
    if i%2==0: ok = True
print(0 if ok else a[0]*a[1])