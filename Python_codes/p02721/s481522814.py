N,K,C = map(int,input().split())
S = list(str(input()))

L = []###i+1回目に働くのはL[i]日目以降
R = []###i+1回目に働くのはL[i]日目以前

for i in range(N):
    if len(L) >= K:
        break
    if S[i] =="o" and (L==[] or (i+1) - L[-1] > C):
        L.append(i+1)

for i in range(N-1,-1,-1):
    if len(R) >= K:
        break
    if S[i] == "o" and (R==[] or R[-1] - (i+1) > C):
        R.append(i+1)

R.reverse()###Rは逆順にappendしたのでreverse
ans = []

for i in range(K):
    if L[i] == R[i]:
        ans.append(L[i])


###
#print(L)
#print(R)
###
for i in range(len(ans)):
    print(ans[i])