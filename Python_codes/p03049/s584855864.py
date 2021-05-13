N = int(input())
cnt, A, B, C = 0, 0, 0, 0
for _ in range(N):
    S = input().rstrip()
    flg = False
    for s in S:
        if s=="A":
            flg=True
        elif flg==True and s=="B":
            cnt += 1
            flg = False
        else: flg = False
    if S[0]=="B": B+=1
    if S[-1]=="A": A+=1
    if S[0]=="B" and S[-1]=="A": C+=1
if A==B==C and A!=0: print(cnt+A-1)
else: print(cnt+min(A,B))