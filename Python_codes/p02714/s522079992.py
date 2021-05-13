N = int(input())
S = input()

A = [0]*3

for s in S:
    if s == "R":
        A[0] += 1
    elif s =="G":
        A[1] += 1
    elif s == "B":
        A[2] += 1
        
ans = 1

for a in A:
    ans *= a

for i in range(N-1):
    for j in range(i+1, N):
        k = 2*j - i
        if(k >= N):
            continue
        if(S[j] != S[i] and S[j] != S[k] and S[i] != S[k]):
            ans -= 1
            
print(ans)