def LI():
    return list(map(int, input().split()))


P, Q, R = LI()
ans = P+Q+R-max(P, Q, R)
print(ans)
