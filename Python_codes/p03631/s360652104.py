n = input()
n_re = n[::-1]
ans = "ok"
for i in range(3):
    if n[i] != n_re[i]:
        ans = "ng"
if ans == "ok":
    print("Yes")
else:
    print("No")