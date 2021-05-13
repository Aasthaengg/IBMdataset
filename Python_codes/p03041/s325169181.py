N, k = input().split()
N = int(N)
k = int(k)
S = input()
S = list(S)

S[k-1] = S[k-1].lower() 
S = "".join(S)
print(S)