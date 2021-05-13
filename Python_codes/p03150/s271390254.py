S = list(input())
tf = [False for _ in range(7)]
key = list("keyence")
for n in range(7):
    if S[n] == key[n]:
        tf[n] = True
    else:
        break
for n in range(1, 8):
    if S[-n] == key[-n]:
        tf[-n] = True
    else:
        break
if all(tf):
    print("YES")
else:
    print("NO")