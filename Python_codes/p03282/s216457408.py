s = input()
k = int(input())
f = True
for si in s[:k]:
    if si != "1":
        print(si)
        f = False
        break
if f: print("1")
