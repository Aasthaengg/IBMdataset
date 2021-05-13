N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))

max_drop = 0
for i in range(N):
    max_drop = max(max_drop, sum(A1[:i+1] + A2[i:]))
print(max_drop)