S = raw_input()
while(S!="-"):
    m = int(raw_input())
    for i in range(m):
        h = int(raw_input())
        S = S[h:] + S[0:h]
    print S
    S = raw_input()