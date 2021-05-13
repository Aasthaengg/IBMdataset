n=int(input())
def out(i):
  print(i,flush=True)
  s=input()
  if s=="Male":return 0
  elif s=="Female":return 1
  else:exit()
f=out(0)
ng=0
ok=n
while ng+1!=ok:
  mid=(ng+ok)//2
  if (mid+f)%2==out(mid)%2:ng=mid
  else:ok=mid