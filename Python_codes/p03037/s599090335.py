n,m=map(int,input().split())
ansl = 1
ansr = n
for i in range(m):
  l,r=map(int,input().split())
  ansl = max(ansl,l)
  ansr = min(ansr,r)
print(max(0,ansr-ansl+1))