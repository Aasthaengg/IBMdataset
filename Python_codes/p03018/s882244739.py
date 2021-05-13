S = input()
newS = S.replace("BC","D")
A_count = 0
ans = 0
for i in range(len(newS)):
    if newS[i] == "A":
        A_count += 1
    elif newS[i] == "D":
        ans += A_count
    else:
        A_count = 0
print(ans)