A, B, K = map(int, input().split())
if K > B-A:
    ans = list(range(A, B+1))
else:
    ans = list(range(A, A+K)) + list(range(B, B - K, -1))
ans = list(set(ans))
ans.sort()
print(*ans, sep='\n')