S = input()
ans = "Yes"
for i in range(len(S)):
    if i%2 == 0 and S[i] == "L":
        ans = "No"
    elif i%2 == 1 and S[i] == "R":
        ans = "No"
print(ans)