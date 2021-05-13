n = int(input())
ca = 0
cb = 0
cab = 0
ans = 0
for i in range(n):
    a = input()
    if a[0] == "B":
        if a[-1] == "A":
            cab += 1
        else:
            cb += 1
    else:
        if a[-1] == "A":
            ca += 1
    for j in range(len(a)-1):
        if a[j] == "A" and a[j+1] == "B":
            ans += 1
if cab == 0:
    print(ans+min(ca,cb))
else:
    if max(ca,cb) > 0:
        print(ans + cab + min(ca,cb))
    else:
        print(ans + cab - 1)