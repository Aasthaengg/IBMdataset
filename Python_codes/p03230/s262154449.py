n = int(input())
flag = 0
a = 0
for i in range(1, 1000):
    if n == a:
        flag = 1
        ans = i-1
        break
    else:
        a += i

if flag == 0:
    print("No")
else:
    print("Yes")
    print(ans+1)
    ans = [[] for j in range(ans+1)]

    l = 1
    c = len(ans)-1
    s = -1
    for i in range(len(ans)):
        for j in range(len(ans)-c-1):
            ans[i].append(ans[j][s])
        for j in range(c):
            ans[i].append(l)
            l += 1
        c -= 1
        s += 1

    for i in range(len(ans)):
        print(len(ans[i]), " ".join(map(str, ans[i])))
