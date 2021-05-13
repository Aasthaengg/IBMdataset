w = input()
D = {}

for i in range(len(w)):
    if w[i] in D:
        D[w[i]] += 1
    else:
        D[w[i]] = 1
for x in D.values():
    if x % 2 == 1:
        print("No")
        break
else:
    print("Yes")