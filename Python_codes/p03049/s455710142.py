import sys,math,collections,itertools
input = sys.stdin.readline

N = int(input())
Aend = []
Bstart = []
Ae_Bs = []
cnt = 0

for i in range(N):
    S = input().rstrip()
    if S[0]=='B' and S[-1] =='A':
        Ae_Bs.append(S)
    elif S[0] == 'B':
        Bstart.append(S)
    elif S[-1] == 'A':
        Aend.append(S)
    cnt += S.count('AB')

lAe_Bs = len(Ae_Bs)
lBstart = len(Bstart)
lAend = len(Aend)

if lAe_Bs >0:
    cnt += lAe_Bs -1
    
if lAe_Bs > 0 and lAend >0:
    cnt += 1
    lAend -=1
if lAe_Bs > 0 and lBstart>0:
    cnt +=1
    lBstart -=1

cnt += min(lAend,lBstart)

print(cnt)
