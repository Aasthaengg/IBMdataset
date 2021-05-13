S = input()

L = {}

ans = "Yes"
for s in S:
    if s in L.keys():
        L[s] += 1
        if L[s] > 2:
            ans = "No"
    else:
        L[s] = 1
if len(L.keys()) != 2:
    ans = "No"

print(ans)
