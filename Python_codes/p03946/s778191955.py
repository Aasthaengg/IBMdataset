N, T = map(int, input().split())
A = [int(c) for c in input().split()]
flag = True
ls = []
st = A[-1]
for i in range(N-2,-1,-1):
  if st-A[i]>0:
    ls += [st-A[i]]
  else:
    st = A[i]
ls.sort()
ans = ls.count(ls[-1])
print(ans)