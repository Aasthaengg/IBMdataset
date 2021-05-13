N = int(input())
res = [0]*4
for i in range(N):
    s = input()
    if s == "AC":
        res[0] += 1
    elif s == "WA":
        res[1] += 1
    elif s == "TLE":
        res[2] += 1
    elif s == "RE":
        res[3] += 1

print(f"AC x {res[0]}")
print(f"WA x {res[1]}")
print(f"TLE x {res[2]}")
print(f"RE x {res[3]}")