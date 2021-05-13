
n = int(input())
s = input()
R = 0
B = 0

for i in range(n):
    if s[i] == "R":
        R += 1
    elif s[i] == "B":
        B += 1

if R - B > 0:
    print("Yes")
else:
    print("No")
