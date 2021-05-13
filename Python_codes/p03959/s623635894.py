import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり


N = I()
T = LI()
A = LI()
mod = 10**9+7

minimum = [1]*N  # 山i(0-index)の高さとしてありうる最小値
maximum = [0]*N  # 山i(0-index)の高さとしてありうる最大値

for i in range(N):
    if i == 0:
        minimum[i] = T[i]
        maximum[i] = T[i]
    else:
        if T[i] != T[i-1]:
            minimum[i] = T[i]
            maximum[i] = T[i]
        else:
            maximum[i] = T[i]

for i in range(N-1,-1,-1):
    if i == N-1:
        minimum[i] = max(minimum[i],A[i])
        maximum[i] = min(maximum[i],A[i])
    else:
        if A[i] != A[i+1]:
            minimum[i] = max(minimum[i],A[i])
            maximum[i] = min(maximum[i],A[i])
        else:
            maximum[i] = min(maximum[i],A[i])

ans = 1
for i in range(N):
    if maximum[i] >= minimum[i]:
        ans *= maximum[i]-minimum[i]+1
        ans %= mod
    else:
        print(0)
        exit()
print(ans)
