N = int(input())
A = [int(i) for i in input().split()]
xorsum = 0
for a in A:
    xorsum = xorsum^a
ans = [xorsum] * N
for i,a in enumerate(A):
    ans[i] = ans[i] ^ a
print(*ans)