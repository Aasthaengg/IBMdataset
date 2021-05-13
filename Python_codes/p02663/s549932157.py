a, b, c, d, k = map(int, input().split())
p = a*60 + b
q = c*60 + d
ans = q-p-k
print(ans)