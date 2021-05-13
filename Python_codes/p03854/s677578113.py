S = input()

S = S[::-1]

check = ["maerd", "remaerd", "esare", "resare"]

ind = 0
f = True

while True:
    if ind == len(S):
        f = True
        break
    if S[ind:ind+5] in check:
        ind += 5
    elif S[ind:ind+6] in check:
        ind += 6
    elif S[ind:ind+7] in check:
        ind += 7
    else:
        f = False
        break

if f:
    print('YES')
else:
    print("NO")