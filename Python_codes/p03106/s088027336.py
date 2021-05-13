A, B, K = [int(n) for n in input().split()]
m = min(A, B)
ans = []
for i in range(1, m+1):
    if A%i==0 and B%i==0:
        ans.append(i)
print(sorted(ans, reverse=True)[K-1])
