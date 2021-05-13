n = int(input())
A = [int(x) for x in input().split()]
A_ = sorted([a - i for i, a in enumerate(A, 1)])
i = len(A) // 2
b = A_[i]
ans = sum([abs(a - b) for a in A_])
print(ans)
