t = input()
t = list(t)

for i in range(len(t)):
    if t[i] == "?":
        t[i] = 'D'
ans = "".join(t)
print(ans)