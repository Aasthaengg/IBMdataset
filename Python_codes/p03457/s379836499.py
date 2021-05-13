n = int(input())
t = [0]
x = [0]
y = [0]
for i in range(n):
    tt, xx, yy = map(int, input().split(" "))
    t.append(tt)
    x.append(xx)
    y.append(yy)

ans = "Yes"
for i in range(n):
    dt = t[i+1] - t[i]
    ddis = abs(x[i + 1] + y[i + 1] - (x[i] + y[i]))
    if not (ddis <= dt and ((dt % 2 == 0 and ddis % 2 == 0) or (dt % 2 == 1 and ddis % 2 == 1))):
        ans = "No"
        break

print(ans)