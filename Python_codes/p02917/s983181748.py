import sys
readline = sys.stdin.readline

N = int(readline())
B = list(map(int,readline().split()))

ans = B[0] + B[-1]
for i in range(len(B) - 1):
  ans += min(B[i + 1],B[i])
  
print(ans)