S = input().strip()
N = len(S)
k = 0
for i in range(N):
    if S[i]=="0":
        k += 1
m = min(k,N-k)
print(2*m)