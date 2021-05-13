n,m = map(int,input().split())
a = []
a_1 = []
a_2 = []
for i in range(m):
    t = list(map(int,input().split()))
    if t[0] == 1:
        a_1.append(t[1])
    if t[1] == n:
        a_2.append(t[0])
    a.append(t)

a = a_1 + a_2
if len(set(a)) < len(a):
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
