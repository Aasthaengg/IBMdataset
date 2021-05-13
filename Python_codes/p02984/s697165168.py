N = int(input())
A = tuple(map(int, input().split()))
ans = 0
for i, a in enumerate(A):
    ans += -a if i & 1 else a
ans //= 2
for a in A:
    print(ans * 2, end=" ")
    ans = a - ans
print()