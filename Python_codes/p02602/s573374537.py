n, k = map(int, input().split())
A = list(map(int, input().split()))
before = sum(A[:k])

for i in range(n-k):
    tmp = before + A[i+k] - A[i]
    if tmp > before:
        print("Yes")
    else:
        print("No")
    before = tmp