N, K, Q = map(int,input().split())
A = [int(input()) for i in range(Q)]

if K > Q:
    for i in range(N):
        print("Yes")

else:
    B = []
    for i in range(N):
        B.append(K - Q)

    for i in range(Q):
        ans = A[i] - 1
        P = B[ans] + 1
        B[ans] = P

    for i in range(N):
        if B[i] > 0:
            print("Yes")
        else:
            print("No")