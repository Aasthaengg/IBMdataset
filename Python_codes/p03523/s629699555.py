t = input()
s = "AKIHABARA"
posA = [0, 4, 6, 8]
ok = 0
pos = [0, 3, 4, 5]
for i in range(2 ** 4):
    tmp = ""
    now = 0
    for j in range(9):
        if j == posA[now]:
            if i >> now & 1:
                tmp = tmp + s[j]
            now += 1
        else:
            tmp = tmp + s[j]

    if t == tmp:
        ok = 1
        break

if ok == 1:
    print("YES")
else:
    print("NO")
