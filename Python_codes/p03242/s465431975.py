n = list(input())
ans = []
for i in range(3):
    if n[i] == "1":
        ans.append("9")
    elif n[i] == "9":
        ans.append("1")
    else:
        ans.append(n[i])
print("".join(ans))