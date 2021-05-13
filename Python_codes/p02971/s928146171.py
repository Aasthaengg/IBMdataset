n = int(input())
a = []
for _ in range(n):a.append(int(input()))

max_ = max(a)
max2 = sorted(a)[-2]
for i in range(n):
    if a[i] != max_:
        print(max_)
    else:
        print(max2)