S = input()
L = len(S)
if S[0] == ">":
    S = "<"+S
else:
    S = ">"+S
if S[L] == ">":
    S = S+"<"
else:
    S = S+">"
count = 0
ans = 0
kari = 0
for i in range(L+1):
    if S[i] == "<" and S[i+1] == ">":
        kari = count
        count = 1
    elif S[i] == ">" and S[i+1] == "<":
        ans += max(kari, count)
        count = 1
    else:
        ans += count
        count += 1

if S[L] == "<" and S[L+1] == ">":
    ans += kari
print(ans)
