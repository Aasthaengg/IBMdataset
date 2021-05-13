N = int(input())
mod = 10**9+7
List = [0,0,1]
if N<=3:
  print(List[N-1])

else:
  for i in range(3,N):
    a = List[-1]+List[-3]
    List.append(a)
  print(List[-1]%mod)