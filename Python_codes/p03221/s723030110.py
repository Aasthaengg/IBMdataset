import bisect
N,M = map(int,input().split())
A = [[] for _ in range(N)] #重複がある場合にはsetにする？
original = []
for i in range(M):
  a,b = map(int,input().split())
  a-=1 #県を0indexに直す
  A[a].append(b)
  original.append((a,b))
for X in A:
  X.sort()
#print(A)
for i in range(M):
  ken,now = original[i]
  ID = bisect.bisect_left(A[ken],now)
  ken += 1; ID+=1
  ans = "0"*(6-len(str(ken)))+str(ken)+"0"*(6-len(str(ID)))+str(ID)
  print(ans)
