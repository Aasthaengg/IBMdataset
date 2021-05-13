n,k = map(int,input().split())
v = list(map(int,input().split()))
m = 0
for i in range(n+1):
  if i > k:
    break
  s = sum(v[:i])
  h = [j for j in v[:i] if j < 0]
  h.sort()
  m = max(m,s-sum(h[:min(len(h),k-i)]))
  for j in range(1,n-i+1):
    if i+j > k:
      break
    cs = s
    cs += sum(v[-j:])
    ch = h[:]
    ch += [j for j in v[-j:] if j < 0]
    ch.sort()
    cs -= sum(ch[:min(len(ch),k-i-j)])
    m = max(m,cs)
print(m)