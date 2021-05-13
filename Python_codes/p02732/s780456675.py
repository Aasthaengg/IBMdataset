from collections import Counter
def solve():
  N = int(input())
  A = list(map(int, input().split()))
  c = Counter(A)
  cnt = 0
  for k,v in c.items():
    cnt += v*(v-1)//2
  ans = [cnt]*N
  for i in range(N):
    ans[i] -= c[A[i]]*(c[A[i]]-1)//2
    ans[i] += (c[A[i]]-1)*(c[A[i]]-2)//2
  
  return ans
print(*solve(),sep='\n')
