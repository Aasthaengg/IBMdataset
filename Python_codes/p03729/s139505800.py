S = input().split()

if S[0][len(S[0])-1] != S[1][0] or S[1][len(S[1])-1] != S[2][0]:
    print("NO")
else:
    print("YES")