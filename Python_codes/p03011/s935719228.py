p, q, r = map(int,input().split())
ans = p + q + r
ans -= max(p,q,r)
print(ans)