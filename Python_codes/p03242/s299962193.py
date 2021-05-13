S = input()
ans = []
for s in S:
    if s == "1":
        ans.append("9")
    elif s == "9":
        ans.append("1")
    else:
        ans.append(s)
print("".join(ans))
