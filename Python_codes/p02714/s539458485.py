import itertools
N=int(input())
S=input()
ans=S.count("R")*S.count("G")*S.count("B")
c=list(itertools.permutations(["R","B","G"],3))
for j in range(1,N):
    for i in range(N-j*2):
        if (S[i],S[i+j],S[i+j*2]) in c:
            ans-=1
print(ans)