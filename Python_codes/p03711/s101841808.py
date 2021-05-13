m = dict()
a0 = [1,3,5,7,8,10,12]
a1 = [4,6,9,11]
a2 = [2]

for i,j in enumerate([a0,a1,a2]):
    for k in j:
        m[k] = i

a, b = map(int, input().split())

if m[a] == m[b]:
    print("Yes")
else:
    print("No")
