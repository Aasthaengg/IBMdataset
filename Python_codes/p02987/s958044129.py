# 132 A

inp = input()
ans = True

for i in inp:
    y = inp.count(i)
    if y != 2:
        ans = False
        break

if ans:
    print("Yes")
else:
    print("No")