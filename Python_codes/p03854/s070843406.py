S = input()
i = 0
n = len(S)
while i <= n-5:
    if S[i:i+5] == "dream":
        i += 5
        if S[i:i+2] == "er" and S[i:i+5] != "erase":
            i += 2
    elif S[i:i+5] == "erase":
        i += 5
        if S[i:i+1] == "r":
            i += 1
    else:
        break
if i != len(S):
    print("NO")
else:
    print("YES")