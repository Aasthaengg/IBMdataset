N, A, B, C, D = map(int, input().split())
S = input()

for i in range(A, C-1):
    if S[i] == "#" and S[i+1] == "#":
        print("No")
        exit()
for i in range(B, D-1):
    if S[i] == "#" and S[i+1] == "#":
        print("No")
        exit()

if A < B and C < D:
    print("Yes")
elif A > B and C < D:
    flag = False
    for i in range(A-2, C-1):
        if S[i] == "." and S[i+1] == "." and S[i+2] == ".":
            flag = True
    if flag:
        print("Yes")
    else:
        print("No")
elif A < B and C > D:
    flag = False
    for i in range(B-2, D-1):
        if S[i] == "." and S[i+1] == "." and S[i+2] == ".":
            flag = True
    if flag:
        print("Yes")
    else:
        print("No")   
else:
    print("Yes")
