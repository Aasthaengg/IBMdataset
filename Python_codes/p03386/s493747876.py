A, B, K = map(int,input().split())

if ((B + 1) - A ) / 2 <= K:
    for i in range(A, B+1):
        print(i)

else:
    for j in range(A, A+K):
        print(j)
    for k in range(B-K+1, B+1):
        print(k)