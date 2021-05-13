MM = input().split()
N = int(MM[0])
M = int(MM[1])
list1 = []
for i in range(M):
  aa = input().split()
  a = int(aa[0])
  b = int(aa[1])
  list1.append(a)
  list1.append(b)
for i in range(1,N+1):
  ans = list1.count(i)
  print(ans)