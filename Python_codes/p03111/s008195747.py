# coding: utf-8
N,A,B,C=map(int,input().split())
L=[]
for i in range(N):
    L.append(int(input()))

def Base_10_to_n(X, base_n, len_N):
    X_dumy = X
    out = ''
    while X_dumy>0:
        out = str(X_dumy%base_n)+out
        X_dumy = int(X_dumy/base_n)
    return out.zfill(len_N)

ans=10**6

for i in range(4**N):
    bit=Base_10_to_n(i,4,N)
    group=[[] for j in range(4)]
    
    for j in range(N):
        group[int(bit[j])].append(L[j])
    
    if not(group[1]) or not(group[2]) or not(group[3]):
        continue
    
    costA = abs(A-sum(group[1])) + (len(group[1])-1)*10
    costB = abs(B-sum(group[2])) + (len(group[2])-1)*10
    costC = abs(C-sum(group[3])) + (len(group[3])-1)*10
    
    cost = costA + costB + costC
    
    ans=min(ans,cost)

print(ans)