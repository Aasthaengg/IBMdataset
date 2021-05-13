N, M = map(int, input().split())
A = list(map(int, input().split()))
s = sum(A)

ans = len([a for a in A if a * 4 * M >= s])

print("Yes" if ans >= M else "No")