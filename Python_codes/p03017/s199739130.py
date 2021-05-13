N, A, B, C, D = map(int, input().split())
S = input()

flg = True
if A < B and C > D:
    flg = False
    for i in range(B-2, D-1):
        if S[i:i+3] == "...":
            flg = True
            break
if A > B and C < D:
    flg = False
    for i in range(A-2, C-1):
        if S[i:i+3] == "...":
            flg = True
            break
for i in range(A-1, C-2):
    if S[i:i+2] == "##":
        flg = False
        break
for i in range(B-1, D-2):
    if S[i:i+2] == "##":
        flg = False
        break

if flg:
    print("Yes")
else:
    print("No")