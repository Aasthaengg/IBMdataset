n = int(input())
ans = [input() for i in range(n)]

cA = ans.count("AC")
print(f"AC x {cA}")
cW = ans.count("WA")
print(f"WA x {cW}")
cT = ans.count("TLE")
print(f"TLE x {cT}")
cR = ans.count("RE")
print(f"RE x {cR}")