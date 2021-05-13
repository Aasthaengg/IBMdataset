n = input()
inp = list(input())
res = 0
for i in inp:
    if i == "R":
        res += 1
    else:
        res -= 1

if res > 0:
    print("Yes")
else:
    print("No")