N, M = map(int, input().split())
A = [int(x) for x in input().split()]

ans=0
for a in A:
  ans = ans + 1 if a*(4*M)>=sum(A) else ans
print('Yes' if ans>=M else 'No')