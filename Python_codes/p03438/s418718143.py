import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

m = sum(B) - sum(A)
if m <= -1:
    print("No")
else:
    # print("m",m)
    M = [m, m]
    for i in range(n):
        di = B[i] - A[i]
        if di > 0:
            if di % 2 == 1:
                di += 1
                M[1] -= 1
            M[0] -= di//2
        else:
            M[1] -= -di
    # print(M)
    if M[0] >= 0 and M[1] >= 0 and M[0]*2 == M[1]:
        print("Yes")
    else:
        print("No")