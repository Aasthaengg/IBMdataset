S = input()
C = ["maerd","remaerd","esare","resare"]
ans = ""
a = "YES"
x = len(S)
for i in range(x):
    ans = ans + S[x - 1 -i]
    if ans == C[0]:
        ans = ""
    elif ans == C[1]:
        ans = ""
    elif ans == C[2]:
        ans = ""
    elif ans == C[3]:
        ans = ""
if len(ans) != 0:
    a = "NO"
print(a)
