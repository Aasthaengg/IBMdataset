N,A,B,C,D = map(int,input().split())
S = input()
if C == D:
    print("No")
    exit()
dot = 0
rock = 0
bol = 0
for i in range(1,N+1):
    if S[i-1] == ".":
        dot += 1
        rock = 0
        if dot >= 3 and B < i <= D + 1:
            bol = 1
    else:
        rock += 1
        dot = 0
        if rock >= 2 and A < i < max(C,D):
            print("No")
            exit()
if C < D:
    print("Yes")
    exit()
print("Yes" if bol == 1 else "No")