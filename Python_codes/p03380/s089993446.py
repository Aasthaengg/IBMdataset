import sys
readline = sys.stdin.readline

N = int(readline())
A = list(map(int,readline().split()))

# 最も大きい数と、その1/2との差が最も小さい数を選ぶ
A = sorted(A, reverse = True)
one = A[0]
diff = one
ans = -1
for i in range(1,len(A)):
  if abs(one / 2 - A[i]) < diff:
    diff = abs(one / 2 - A[i])
    ans = A[i]
    
print(one, ans)