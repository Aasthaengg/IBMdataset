A = list(map(int, input().split()))

ans = "No"

if abs(A[0]-A[2]) <= A[3]:
    ans = "Yes"

if abs(A[1]-A[0]) <= A[3] and abs(A[2]-A[1]) <= A[3]:
    ans = "Yes"

print(ans)