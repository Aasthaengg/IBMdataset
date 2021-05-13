S, T = input(), input()
d = dict()
count = 0
S_list = []
for c in S:
    try:
        n = d[c]
    except:
        d[c] = n = count
        count += 1
    S_list.append(n)
d = dict()
count = 0
for m, c in zip(S_list, T):
    try:
        n = d[c]
    except:
        d[c] = n = count
        count += 1
    if n != m:
        print("No")
        break
else:
    print("Yes")