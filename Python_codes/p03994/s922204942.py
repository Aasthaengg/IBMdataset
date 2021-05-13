S=list(input())
K=int(input())
N=len(S)

for i in range(N):
    if S[i]=="a":
        continue
    sa=ord("z")-ord(S[i])+1
    if sa<=K:
        K-=sa
        S[i]="a"

if K!=0:
    K%=26
    S[i]=chr(ord(S[i])+K)

print("".join(S))