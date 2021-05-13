x = input()

ans = len(x)
l = 0
r = 0
for i in range(len(x)):
    if x[i] == "S":
        l += 1
    else:
        l -= 1

        if l < 0:
            l = 0
        else:
            ans -= 2

print(ans)