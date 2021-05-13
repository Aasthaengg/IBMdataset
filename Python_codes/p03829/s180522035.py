N, A, B = map(int, input().split())
x = tuple(map(int, input().split()))
k = B//A

res = 0
for i in range(N-1):
    if x[i+1]-x[i] > k:
        res += B
    else:
        res += (x[i+1]-x[i])*A
print(res)