s = input()
xlist = []
xcount = 0
t = ""
for i in range((len(s))):
    if s[i] == "x":
        xcount += 1
    else:
        xlist.append(xcount)
        xcount = 0
        t += s[i]
xlist.append(xcount)
if t != t[::-1]:
    print(-1)
else:
    ans = 0
    for i in range(len(xlist)//2):
        ans += abs(xlist[i]-xlist[-(i+1)])
    print(ans)