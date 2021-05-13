N = int(input())
A = list(map(int, input().split()))

ave = sum(A) / N
ans = 0
diff = ave
for i in range(N):
    d = abs(A[i] - ave)
    if diff > d:
        diff = d
        ans = i

print(ans)
