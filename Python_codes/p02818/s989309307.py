a,b,k = map(int, input().split())

res_a = max(0, a-k)
res_b = max(0, b-(k-a)) if k-a>0 else b

print(res_a, res_b)