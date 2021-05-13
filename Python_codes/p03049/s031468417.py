import sys,math,collections,itertools
input = sys.stdin.readline

N = int(input())
lAend = 0
lBstart = 0
lAe_Bs = 0
cnt = 0

for i in range(N):
    S = input().rstrip()
    if S[0]=='B' and S[-1] =='A':
        lAe_Bs+=1
    elif S[0] == 'B':
        lBstart+=1
    elif S[-1] == 'A':
        lAend+=1
    cnt += S.count('AB')

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
