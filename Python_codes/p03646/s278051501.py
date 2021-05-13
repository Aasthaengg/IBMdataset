import sys
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
mod = 10**9 + 7
inf = float('inf')

K = I()
ans = int(50)
ansC = [0]*50
for i in range(50):
    ansC[i] = ((K+i)//50)+i

"""
ansC[0] +=(K+1)
ansC[0] -= (K // 2)
ansC[1] += (K // 2)
"""
print(ans)
print(" ".join(map(str,ansC)))

