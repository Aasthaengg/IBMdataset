N = int(input())
A = tuple(map(int, input().split()))
ans = [str(i + 1) for a, i in sorted((a, i) for i, a in enumerate(A))]
print(" ".join(ans))