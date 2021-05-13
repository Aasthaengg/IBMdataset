s = input()
t = input()
ds = dict()
dt = dict()
ni = 1
for i in range(len(s)):
    si = s[i]
    ti = t[i]
    if not si in ds:
        ds[si] = ni
        if ti in dt:
            print("No")
            exit()
        else:
            dt[ti] = ni
            ni += 1
    elif (not ti in dt) or (not ds[si] == dt[ti]):
        print("No")
        exit()

print("Yes")
