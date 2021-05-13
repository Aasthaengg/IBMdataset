S = list(input())
N = len(S)
#print('S',S)

dammy1=[0]*(N+1)
A=0
for i in range(1,N+1):
    if S[i-1]=='<':
        A+=1
        dammy1[i]=A
    elif S[i-1]=='>':
        A=0
        dammy1[i]=A

dammy2=[0]*(N+1)
B=0
for i in range(1,N+1):
    if S[-i]=='>':
        B+=1
        dammy2[-(i+1)]=B
    elif S[-i]=='<':
        B=0
        dammy2[-(i+1)]=B

#print('dammy1', dammy1)
#print('dammy2', dammy2)

out=[0]*(N+1)
for i in range(N+1):
    out[i] = max(dammy1[i], dammy2[i])

#print('out', out)
print(sum(out))