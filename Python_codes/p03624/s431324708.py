S = input()
al = [0] * 26
s = ""

for s in S:
    al[ord(s) - 97] += 1

if 0 not in al:
    print("None")
else:
    print(chr(al.index(0) + 97))