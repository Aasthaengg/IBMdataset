def linearSearch(S, N, key):
    i = 0
    S[N] = key
    while S[i] != key:
        i += 1
    if i != N:
        return True
    
N = int(input())
S = list(map(int,input().split()))
q = int(input())
T = list(map(int,input().split()))  

S.append(0)

sum = 0 

for j in range(q):
    if linearSearch(S,N,T[j]) == True:
        sum += 1
    
print(sum)
