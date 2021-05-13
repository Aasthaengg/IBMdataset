s = input()
cf = ""
for e in s:
    if e in ["C", "F"]:
        cf += e

if cf.count("CF"):
    ans = "Yes"
else:
    ans = "No"

print(ans)
