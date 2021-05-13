from sys import stdin
def LI(): return list(map(int,stdin.readline().rstrip().split()))
li = LI()

n,k = [li.pop(0) for i in range(2)]

ans = k
for i in range(1,n):
    ans *= (k-1)

print(ans)