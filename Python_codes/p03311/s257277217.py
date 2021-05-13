N = int(input())
A = list(map(int, input().split()))
B = [0] * N
for i, a in enumerate(A):
    B[i] = a - i - 1
B.sort()
b = B[N//2]
ans = 0
for j in B:
    ans += abs(j - b)
print(ans)
