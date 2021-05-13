p, q, r = map(int, input().split())
ABC = p + q
ACB = r + q
BAC = p + r
ans = min((ABC, ACB, BAC))
print(ans)