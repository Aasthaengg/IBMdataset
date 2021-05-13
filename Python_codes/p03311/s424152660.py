N = int(input())
A = list(map(int, input().split()))
A = sorted([a - i for i, a in enumerate(A, 1)])

b = A[(N - 1)//2]
ans = sum([abs(a-b) for a in A])
print(ans)