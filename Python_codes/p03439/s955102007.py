def printt(x):
  print(x,flush=True)
  i=input()
  if i=="Vacant":exit()
  if i=="Male":return 0
  return 1
n=int(input())
ng=0
ok=n
f=printt(0)
while ng+1!=ok:
  mid=(ok+ng)//2
  if printt(mid)==(f+mid)%2:ng=mid
  else:ok=mid