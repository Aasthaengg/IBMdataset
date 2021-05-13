N = int(input())
A = sorted(map(int, input().split()), reverse=True)
ans = sum(A[:N//2]) + sum(A[1:-(-N//2)])
print(ans)
