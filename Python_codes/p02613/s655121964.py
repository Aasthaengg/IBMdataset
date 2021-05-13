n = int(input())
AC = 0
TLE = 0
WA = 0
RE = 0
for i in range (0, n):
    a = input()

    if a == "AC":
        AC += 1
    elif a == "TLE":
        TLE += 1
    elif a == "WA":
        WA += 1
    elif a == "RE":
        RE += 1

print("AC x", AC)
print("WA x", WA)
print("TLE x", TLE)
print("RE x", RE)