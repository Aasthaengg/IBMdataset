x = list(input())
s, t = 0, 0
ans = 0
for i in range(len(x)):
    if x[i] == "T":
        t += 1
        if s > 0:
            s -= 1
            t -= 1
    else:
        s += 1
print(s + t)