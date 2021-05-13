S=list(input())
N=len(S)

cnt_g=0
cnt_p=0

for i in range(N):
    if S[i]=="g":
        cnt_g+=1
    else:
        cnt_p+=1

ans=(cnt_g-cnt_p)//2

print(ans)
