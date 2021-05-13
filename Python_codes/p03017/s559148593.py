N,A,B,C,D = map(int, input().split())
S = input()

ans = "Yes"
if C < D:
    for i in range(A-1, C-1):
        if S[i] == "#" and S[i+1] == "#":
            ans = "No"
    for i in range(B-1, D-1):
        if S[i] == "#" and S[i+1] == "#":
            ans = "No"
else:
    for i in range(A-1, C-1):
        if S[i] == "#" and S[i+1] == "#":
            ans = "No"
    flag = True
    for i in range(B-2, D-1):
        if S[i] == "." and S[i+1] == "." and S[i+2] == ".":
            flag = False
    if flag:
        ans = "No"
print(ans)