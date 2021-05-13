n, a, b, c = map(int, input().split())
l = [int(input()) for i in range(n)]
min_ = 10**18
for i in range(4**n):
  la = []
  lb = []
  lc = []
  for j in range(n):
    i, amari = divmod(i, 4)
    if amari == 1:
      la.append(l[j])
    elif amari == 2:
      lb.append(l[j])
    elif amari == 3:
      lc.append(l[j])
    
    if len(la)>0 and len(lb)>0 and len(lc)>0:
      min_ = min(min_, abs(sum(la)-a)+10*(len(la)-1)+abs(sum(lb)-b)+10*(len(lb)-1)+abs(sum(lc)-c)+10*(len(lc)-1))
      
print(min_)