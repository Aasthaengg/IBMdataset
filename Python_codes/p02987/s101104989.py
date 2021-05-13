S = list(input())
w = {}
for s in S:
    if w.get(s) == None:
        w[s] = 1
    else:
        w[s] += 1

if len(w) == 2 and sum(w.values()) == 4:
    print("Yes")
else:
    print("No")
