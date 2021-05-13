S = list(input())
N = len(S)

out=[]
for i in range(N-2):
    X = 100*int(S[i]) + 10*int(S[i+1]) + int(S[i+2])
    out.append(abs(753-X))

print(min(out))