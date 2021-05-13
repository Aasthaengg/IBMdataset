N,K,C = map(int,input().split())
S = list(input())
W = [i for i in range(N) if S[i]=="o" ]
# print(W)

def LR(S,f):
    D = {}
    i = 0
    count = 0
    while i<N and count<K:
        if S[i] == "o":
            count += 1
            if f:
                D[count] = i
            else:
                D[m+1-count] = N-1 - i
            i += C
        i += 1
    return D

L = LR(S,True)
m = max(L)
S.reverse()
R = LR(S,False)
# print(L,R)

for i in range(1,m+1):
    if L[i]==R[i]:
        print(L[i]+1)