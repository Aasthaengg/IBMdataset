import itertools,sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
N = I()
A = LI()
ans = 0
for x in [x for x in itertools.product([-1,0,1],repeat=N)]:
    calc = 1
    for i in range(N):
        calc *= A[i]+x[i]
    if calc%2==0:
        ans += 1
print(ans)
