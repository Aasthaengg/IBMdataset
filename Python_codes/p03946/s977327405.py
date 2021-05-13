import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N,T = LI()
A = LI()

m = A[-1]
ans = []
for i in range(N-2,-1,-1):
    ans.append(m-A[i])
    m = max(m,A[i])

print(ans.count(max(ans)))