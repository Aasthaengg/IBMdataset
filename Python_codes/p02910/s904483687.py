S = list(input())

ans = "Yes"
for i in range(len(S)):
    cnt = i +1
    if cnt % 2 != 0:
        if S[i] == "L":
            ans = "No"
            break
    else:
        if S[i] == "R":
            ans = "No"
            break
print(ans)