S = input()
s = len(S)
T = input()
t = len(T)

key = 0
for i in range(s-t,-1,-1):
    for j,k in enumerate(S[i:i+t]):
        if k == T[j] or k =="?":
            pass
        else:
            break
    else:
        key = i
        break
    key = 100
if key == 100 or s<t:
    print("UNRESTORABLE")
else:
    ans = S[0:i]+T+S[i+t:]
    ans = ans.replace("?","a")
    print(ans)