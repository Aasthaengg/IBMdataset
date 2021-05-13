import sys
sys.setrecursionlimit(10**8)

K = int(input())

for i in [2,5]:
    if K%i==0:
        print(-1)
        exit()
t = 0
for i in range(K):
    t = (t*10+7)%K
    if t == 0:
        print(i+1)
        exit()
print(-1)