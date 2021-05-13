S = input()
T = input()

n = len(S)
m = len(T)

res = []

for i in range(n-m+1):
    for j in range(m):
        if S[i+j] != "?":
            if S[i+j] != T[j]:
                break
    else:
        text = ""
        for x in S[:i]+T+S[i+m:]:
            if x == "?":
                text += "a"
            else:
                text += x
        res.append(text)

if res:
    print(min(res))
else:
    print("UNRESTORABLE")