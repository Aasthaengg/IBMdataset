P, Q, R = map(int, input().split())
print(min(P+Q, R+Q, P+R, Q+R, R+P, Q+P))