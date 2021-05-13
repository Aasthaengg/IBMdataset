K, N = map(int, input().split())
A = list(map(int, input().split()))
diff = []
for i in range(N):
    if A[i-1] > A[i]:
        diff.append(A[i]-(A[i-1]-K))
    else:
        diff.append(A[i]-(A[i-1]))

print(sum(sorted(diff)[:-1]))