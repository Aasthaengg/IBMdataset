N = int(input())
A = list(map(int, input().split()))
S = set(A)
if len(S) > 3:
    print("No")
elif len(S) == 1:
    if A[0] == 0:
        print("Yes")
    else:
        print("No")
elif len(S) == 2:
    if A.count(0) == N // 3 and N % 3 == 0:
        print("Yes")
    else:
        print("No")
else:
    L = list(S)
    y = L[0] ^ L[1] ^ L[2]
    if all(A.count(x) == N // 3 for x in S) and N % 3 == y == 0:
        print("Yes")
    else:
        print("No")