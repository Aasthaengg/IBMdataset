import sys
input = sys.stdin.readline
N,M= map(int,input().rstrip().split())
island = []
for _ in range(M):
  a, b = map(int,input().rstrip().split())
  island.append((a,b))
end_sort = sorted(island,key = lambda x:x[1])
ans = 0
cut = -float('inf')
for i in range(M):
  if cut <= end_sort[i][0]:
    ans += 1
    cut = end_sort[i][1]
print(ans)