from collections import defaultdict
n = int(input())
name_d = dict()
name_d["M"] = 0
name_d["A"] = 0
name_d["R"] = 0
name_d["C"] = 0
name_d["H"] = 0

for _ in range(n):
    s = input()
    if s[0] in "MARCH":
        name_d[s[0]] += 1
#print(name_d)
name_patturn = ["MAR", "MRC", "MCH", "MAH", "MAC", "MRH", "ARC", "ARH", "ACH", "RCH"]
ans = 0
for patturn in name_patturn:
    ans += name_d[patturn[0]]*name_d[patturn[1]]*name_d[patturn[2]]

print(ans)
