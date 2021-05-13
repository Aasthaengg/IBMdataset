S = input()

ans = len(S)

abc = "abcdefghijklmnopqrstuvwxyz"

def do(x,c):
    if x.count(c)==len(x):
        return 0
    res = ""
    for i in range(len(x) - 1):
        if (x[i]==c or x[i+1]==c):
            res += c
        else:
            res += x[i]
    return 1+do(res,c)

for c in abc:
    ans = min(ans,do(S,c))

print(ans)