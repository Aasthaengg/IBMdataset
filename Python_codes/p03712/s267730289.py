H,W=map(int,input().split())

S=["#"*(W+2)]
for _ in range(H):
    S.append("#"+input()+"#")
S.append("#"*(W+2))

for s in S:
    print(s)
