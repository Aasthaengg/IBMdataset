N=int(input())
N_max=10**5

Trig=[0]
k=1
T=0
while T<=N_max:
    T+=k
    k+=1
    Trig.append(T)

try:
    K=Trig.index(N)+1
except:
    print("No")
    exit()
S=[set() for _ in range(K)]
m=0
for i in range(K):
    for j in range(i+1,K):
        m+=1
        S[i].add(m)
        S[j].add(m)

print("Yes")
print(K)
X=[""]*K
for i in range(K):
    X[i]="{} ".format(len(S[i]))+" ".join(map(str,S[i]))

print("\n".join(X))