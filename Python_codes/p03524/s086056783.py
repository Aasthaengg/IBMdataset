S = input().strip()
N = len(S)
C = {"a":0,"b":0,"c":0}
for i in range(N):
    C[S[i]] += 1
na = C["a"]
nb = C["b"]
nc = C["c"]
if max(na,nb,nc)-min(na,nb,nc)<=1:
    print("YES")
else:
    print("NO")