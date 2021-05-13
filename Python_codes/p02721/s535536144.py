N,K,C = list(map(int,input().split()))
S = list(input())
L = []
R = []
life = 0
cnt = K
for i in range(N):
    if cnt==0:
        break
    if S[i]=="o":
        if life <= 0:
            life = C
            L.append(i)
            cnt += -1
        else:
            life += -1
    elif S[i]=="x":
        life += -1

life = 0
cnt = K
for i in range(N):
    if cnt==0:
        break
    if S[N-1-i]=="o":
        if life <= 0:
            life = C
            R.append(N-1-i)
            cnt += -1
        else:
            life += -1
    elif S[N-1-i]=="x":
        life += -1

L.sort()
R.sort()
for i in range(min(len(L),len(R))):
    if L[i]==R[i]:
        print(L[i]+1)