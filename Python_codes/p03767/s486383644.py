N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)
ans = sum(A[:2 * N][1::2])
print(ans)
