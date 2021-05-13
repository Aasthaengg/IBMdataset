N = int(input())
C0 = C1 = C2 = C3 = 0
for _ in range(N):
    S = input()
    if S == "AC":
        C0 += 1
    elif S == "WA":
        C1 += 1
    elif S == "TLE":
        C2 += 1
    elif S == "RE":
        C3 += 1

print("AC x %d"%C0)
print("WA x %d"%C1)
print("TLE x %d"%C2)
print("RE x %d"%C3)
