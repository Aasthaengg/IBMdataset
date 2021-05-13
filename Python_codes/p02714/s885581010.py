N=int(input())
S=input()

R,G,B=0,0,0
for i in range(N):
    if S[i]=="R":
        R+=1
    elif S[i]=="G":
        G+=1
    else:
        B+=1

rest=0
for i in range(N):
    for j in range(i,N):
        k=2*j-i
        if k>=N:
            break
        if S[i]!=S[j] and S[j]!=S[k] and S[k]!=S[i]:
            rest+=1

ans=R*G*B-rest

print(ans)