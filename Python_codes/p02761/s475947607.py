def main():
  N, M = map(int,input().split())
  dct = {}
  ans = [0]*N
  for _ in range(M):
    s, c = map(int,input().split())
    ans[s-1]=c
    if s==1 and c==0 and N>=2:
      print(-1)
      return
    elif s not in dct:
      dct[s] = c
    else:
      if dct[s]!=c:
        print(-1)
        return 
  if ans[0]==0 and N>=2:
    ans[0]=1
  res = 0
  for i in ans:
    res*=10
    res+=i
  print(res)
  return
main()