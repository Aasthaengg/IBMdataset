import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N = I()
a = LI()

s,t = 0,0  # 4の倍数の個数、4の倍数でない偶数の個数
for i in range(N):
    if a[i] % 4 == 0:
        s += 1
    elif a[i] % 2 == 0:
        t += 1

if s >= N//2 or t >= N-2*s:
    print('Yes')
else:
    print('No')