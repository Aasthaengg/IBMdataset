n = int(input())
s = input()
r,b = 0,0
for i in range(n):
    if s[i] == "R":
        r += 1
    else:
        b += 1
if r > b:
    print("Yes")
else:
    print("No")