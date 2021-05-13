N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = sum(B) - sum(A)
a, b = cnt, cnt
for i in range(N):
    if A[i] < B[i]:
        b -= (B[i]-A[i]+1)//2
    elif A[i] > B[i]:
        a -= A[i]-B[i]
    if a < 0 or b < 0:
        print("No")
        break
else:
    print("Yes")