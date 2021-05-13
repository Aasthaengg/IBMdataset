n, m = map(int,input().split())
lst = []
for i in range(m):
    lst.append(list(map(int,input().split())))

min = lst[0][0]
max = lst[0][1]
for v in lst:
    if v[0] > min:
        min = v[0]
    if v[1] < max:
        max = v[1]
if min <= max:
    print(max-min + 1)
elif min > max:
    print(0)
