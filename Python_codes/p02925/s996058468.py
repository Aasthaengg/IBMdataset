import sys
N = int(input())
T = []
for i in range(N):
    a = [i-1 for i in map(int,input().split())]
    T.append(a)

update = list(range(N))
ans = 0
L = [N-1]*N
while(True):
    K = []
    M = [0]*N
    for i in update:
        if L[i] != 0 and M[i] == 0:
            s = T[i][0]
            if L[s] != 0:
                if T[s][0] == i and M[s] == 0:
                    K.append(i)
                    K.append(s)
                    M[i] = 1
                    M[s] = 1
    for j in K:
        del T[j][0]
        L[j] -= 1
    if len(K) == 0:
        break
    ans += 1
    update = K

for i in range(N):
    if L[i] != 0:
        print(-1)
        sys.exit()
print(ans)