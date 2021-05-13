s = input()
t = "AKIHABARA"
idx = 0
ng = 0
for i in range(len(t)):
    if t[i] == s[idx]:
        idx += 1
    elif t[i] != "A":
        ng = 1
        break
    if idx == len(s):
        if i < len(t) - 2:
            ng = 1

        break

if idx != len(s):
    ng = 1

if ng:
    print("NO")
else:
    print("YES")
