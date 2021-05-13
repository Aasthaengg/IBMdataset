n = int(input())
x1 = 0
x2 = 0
x3 = 0
x4 = 0
for i in range(n):
    s = input()
    if s == "AC":
        x1 += 1
    elif s == "WA":
        x2 += 1
    elif s == "TLE":
        x3 += 1
    elif s == "RE":
        x4 += 1
print("AC x", x1)
print("WA x", x2)
print("TLE x", x3)
print("RE x", x4)