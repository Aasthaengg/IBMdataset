#49B
H,W=map(int,(input().split()))
C=[input() for i in range(H)]
ans = ""
for i in range(H):
    ans = ans + C[i] + '\n'+C[i]+'\n'
print(ans[:-1])