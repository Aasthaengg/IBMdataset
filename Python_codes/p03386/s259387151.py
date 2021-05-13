A, B, K = map(int, input().split())

tmp_s = {i for i in range(A, A+K)}
tmp_l = {i for i in range(B+1-K, B+1)}

ans = list(tmp_s.union(tmp_l))
ans = [i for i in ans if A<=i<=B]
ans.sort()

print(*ans, sep="\n")