N,K = map(int,input().split())
V = list(map(int,input().split()))
max_cnt = -float('inf')
for k in range(min(N,K)+1):
  for i in range(k+1):
    j = k - i
    le = V[:i]
    ri = V[-j:] if j > 0 else []
    ne = [i for i in le if i < 0]+[j for j in ri if j < 0]
    ne.sort()
    max_cnt = max(sum(le)+sum(ri) - sum(ne[:K-k]),max_cnt)
    
print(max_cnt)