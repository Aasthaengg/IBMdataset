P, Q, R = map(int, input().split())
ans = []

ans.append(P+Q)
ans.append(Q+R)
ans.append(R+P)

print(min(ans))