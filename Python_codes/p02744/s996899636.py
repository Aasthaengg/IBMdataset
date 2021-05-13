import sys
def I(): return int(sys.stdin.readline().rstrip())

N = I()

ANS = [[] for _ in range(N+1)]

for i in range(1,N+1):
    if i == 1:
        ANS[i].append('a')
    else:
        for a in ANS[i-1]:
            for j in range(97,ord(max(a[k] for k in range(i-1)))+2):
                ANS[i].append(a+chr(j))
print(*ANS[N],sep='\n')
