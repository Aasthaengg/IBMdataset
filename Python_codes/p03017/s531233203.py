N, A, B, C, D = map(int, input().split())
S = ["#"] + list(input())

flag = True
for i in range(A, C):
    if S[i] == "#" and S[i + 1] == "#":
        flag = False
        break
else:
    for i in range(B, D):
        if S[i] == "#" and S[i + 1] == "#":
            flag = False
            break

if flag:
    if C < D:
        print("Yes")
    else:
        for i in range(B, D + 1):
            if S[i - 1] == "." and S[i] == "." and S[i + 1] == ".":
                print("Yes")
                break
        else:
            print("No")
else:
    print("No")
