n = int(input())

judge = {"AC": 0, "WA": 0, "TLE": 0, "RE": 0}
for _ in range(n):
	s = input()
	judge[s] += 1

print("AC x", judge["AC"])
print("WA x", judge["WA"])
print("TLE x", judge["TLE"])
print("RE x", judge["RE"])
