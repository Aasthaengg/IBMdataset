S = list(map(int, input().split()))
P = S[0]
Q = S[1]
R = S[2]
print(min(P+Q, Q+R, R+P))