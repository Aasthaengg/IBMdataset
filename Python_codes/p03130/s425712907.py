miti = [[] for _ in range(5)]

for i in range(3):
    a, b = map(int, input().split())
    miti[a].append(b)
    miti[b].append(a)

cnt_list = []

for m in miti:
    cnt_list.append(len(m))
cnt_list.sort()
if cnt_list == [0, 1, 1, 2, 2]:
    print("YES")
else:
    print("NO")
