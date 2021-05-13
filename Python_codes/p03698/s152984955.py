S = input()
al = [0] * 26
s = ""
for s in S:
    al[ord(s) - 97] += 1

for a in al:
    if a >= 2:
        s = "no"
        break
    else:
        s = "yes"

print(s)