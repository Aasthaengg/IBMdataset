n=int(input())
P=list(map(int,input().split()))
S=sorted(P)
c=0
ans="NO"
for i in range(n):
    if P[i]!=S[i]:
        c+=1
if c<=2 :
    ans ="YES"
print(ans)