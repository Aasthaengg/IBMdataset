N = int(input())

A = [int(x) for x in input().split()]

ans = max(A) - min(A)
print(ans)