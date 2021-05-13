N = int(input())
S = [input().strip() for _ in range(N)]
C = {"A":0,"B":0,"BA":0}
cnt = 0
for i in range(N):
    s = S[i]
    for j in range(len(s)-2+1):
        if s[j:j+2]=="AB":
            cnt += 1
    if s[0]=="B" and s[-1]=="A":
        C["BA"] += 1
    elif s[0]=="B":
        C["B"] += 1
    elif s[-1]=="A":
        C["A"] += 1
if C["BA"]>0:
    cnt += C["BA"]-1
    if C["B"]>0:
        cnt += 1
        C["B"] -= 1
    if C["A"]>0:
        cnt += 1
        C["A"] -= 1
cnt += min(C["B"],C["A"])
print(cnt)