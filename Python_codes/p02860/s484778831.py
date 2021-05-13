N = int(input())
S = str(input())

if N % 2 == 0:
    M = int(N/2)
    if S[:M] == S[M:]:
        print("Yes")
    else:
        print("No")
else:
    print("No")
