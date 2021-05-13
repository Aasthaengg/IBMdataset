H,W = map(int,input().split())
S = [""]
for i in range(W + 2):
    S[0] += "#"
for i in range(H):
    S.append("#" + input() + "#")

S.append("")
for i in range(W + 2):
    S[H  + 1] += "#"

for s in S:
    print(s)

