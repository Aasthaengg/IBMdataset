N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
sa = sum(A)
sb = sum(B)
if sa>sb:
    print("No")
else:
    d1 = 0
    d2 = 0
    for i in range(N):
        if A[i]>B[i]:
            d1 += A[i]-B[i]
        elif B[i]>A[i]:
            d2 += (B[i]-A[i])//2
    if d2>=d1:
        print("Yes")
    else:
        print("No")