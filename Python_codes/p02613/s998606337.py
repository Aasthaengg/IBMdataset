N = int(input())

AC = 0
WA = 0
TLE = 0
RE = 0

Z = 0

for i in range(N):
    Z = input()
    if Z == 'AC':
        AC += 1
    elif Z == 'WA':
        WA += 1
    elif Z == 'TLE':
        TLE += 1
    elif Z == 'RE':
        RE += 1
    else:
        continue

print("AC x", AC)
print("WA x", WA)
print("TLE x", TLE)
print("RE x", RE)