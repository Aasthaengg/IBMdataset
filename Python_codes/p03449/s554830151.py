N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ma = 0
for i in range(N):
    c = sum(A[:i+1]) + sum(B[i:])
    ma = max(ma, c)
print(ma)
