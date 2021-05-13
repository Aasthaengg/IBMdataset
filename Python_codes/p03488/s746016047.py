s = input()
xy = list(map(int,input().split()))
data = [[0],[0]]
direct = 0
for i in s:
    if i == "F":
        data[direct][-1] += 1
    else:
        direct ^= 1
        data[direct].append(0)
judge = [False, False]
for direct in range(2):
    set_now = set((data[direct][0],))
    for d in data[direct][1:]:
        s_next = set()
        for e in set_now:
            s_next.add(e+d)
            s_next.add(e-d)
        set_now = s_next

    if xy[direct] in set_now:
        judge[direct] = True

if judge[0] and judge[1]:
    print("Yes")
else:
    print("No")