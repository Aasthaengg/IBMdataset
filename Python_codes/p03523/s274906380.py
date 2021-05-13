def f(i):
    if i == ls + 1:
        for j in range(ls + 1):
            if u[j] == 1:
                t[2 * j] = "A"
            else:
                t[2 * j] = ""
        if "".join(t) == "AKIHABARA":
            print("YES")
            exit()
        return
    u[i] = 1
    f(i + 1)
    u[i] = 0
    f(i + 1)

s = list(input())
ls = len(s)
if ls >= 10:
    print("NO")
    exit()
t = ["" for _ in range(2 * ls + 1)]
for i in range(ls):
    t[2 * i + 1] = s[i]
n = ls + 1
u = [0] * n
f(0)
print("NO")