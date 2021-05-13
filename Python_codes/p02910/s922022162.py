S=input()
ans = 1
for i in range(len(S)):
    if i % 2 == 0:
        if S[i] == "L":
            ans = 0
            break
    else:
        if S[i] == "R":
            ans = 0
            break
if ans:
    print("Yes")
else:
    print("No")