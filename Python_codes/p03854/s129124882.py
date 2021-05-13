S=input()
N=len(S)
strings = ["maerd", "remaerd", "esare", "resare"]
tmp = ""
for i in range(N-1, -1, -1):
    if tmp not in strings:
        tmp += S[i]
        if tmp in strings:
            tmp = ""
if tmp:
    print("NO")
else:
    print("YES")