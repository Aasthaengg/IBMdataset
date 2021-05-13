S = list(map(int, input().split()))
A = S[0]*60 + S[1]
B = S[2]*60 + S[3]
print(B-A-S[4])
