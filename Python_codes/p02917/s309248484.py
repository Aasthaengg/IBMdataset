N=int(input())
S=list(map(int,input().split()))
Z=[]
Z.append(S[0])
for i in range(N-2):
    Z.append(min(S[i],S[i+1]))
Z.append(S[N-2])
print(sum(Z))

