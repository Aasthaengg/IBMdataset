s = input()
q = int(input())
mae,usiro = [],[]

f = 0
for i in range(q):
    t = input().split()
    if t[0] == "1":
        if f % 2 == 0:
            f = 1
        else:
            f = 0
    elif t[0] == "2":
        if t[1] == "1":
            if f == 1:
                usiro.append(t[2])
            else:
                mae.append(t[2])
        elif t[1] == "2":
            if f == 1:
                mae.append(t[2])
            else:
                usiro.append(t[2])

mae = mae[::-1]
ans = "".join(mae)+s+"".join(usiro)
if f:
    print(ans[::-1])
else:
    print(ans)
