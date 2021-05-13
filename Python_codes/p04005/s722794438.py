l = list(map(int, input().split()))
l = sorted(l)
for i in l:
    if i % 2 == 0:
        print(0)
        break
else:
    print(l[0] * l[1])