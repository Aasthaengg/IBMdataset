S = list(input().replace("BC", "X"))
N = len(S)
pos, ans = 0, 0
ca = 0

while pos<N:
    ca = 0
    if S[pos]=="A" or S[pos]=="X":
        while pos<N and (S[pos]=="A" or S[pos]=="X"):
            if S[pos]=="A":
                ca += 1
            else:
                ans += ca
            pos += 1
    else:
        pos += 1

print(ans)