A = list(map(int, input().split()))
res = 0
for i in range(len(A)):
    res += A[i]
if res > 21:
    print("bust")
else:
    print("win")