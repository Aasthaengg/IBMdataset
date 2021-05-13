N, M = [int(i) for i in input().split()]

# S used all C
if 2*N >= M:
    ans = int(M//2)
else:
    ans = N
    M = M - 2*N
    ans += int(M//4)
print(ans)