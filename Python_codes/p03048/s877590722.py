import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
R,G,B,N = LI()
ans = 0
for i in range(N+1):
    for j in range(N+1):
        temp = N-(R*i+G*j)
        if temp>=0 and temp%B==0:
            ans += 1
print(ans)