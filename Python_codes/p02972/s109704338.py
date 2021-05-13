import sys
sys.setrecursionlimit(10000000)
mod = 10**9 + 7
#mod = 9982443453
def readInts():
  return list(map(int,input().split()))
def I():
  return int(input())
n = I()
A = readInts()
ans = []
for i in reversed(range(n)):
    if A[i]:
        ans.append(i+1)
        tmp = 1
        n = i+1
        while tmp*tmp <= n:
            if n%tmp == 0:
                A[tmp-1] ^= 1
                if tmp != n//tmp:
                    A[n//tmp-1]^=1
            tmp += 1
if len(ans) > 0:
    print(len(ans))
    print(*ans)
else:
    print(0)
