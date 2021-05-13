N = int(input())
A = list(map(int,input().split()))
if sum(A) ==0: #すべてゼロ
  print("Yes")
  exit()

if N%3 != 0:
  print("No")
else:
  dic = {}
  for x in A:
    if x in dic:
      dic[x] += 1
    else:
      dic[x] = 1
  V = list(dic.values())
  if len(V) == 2:
    K = list(dic.keys())
    if K[0] == 0 and dic[K[1]] == dic[0]*2:
      print("Yes")
    elif K[1] == 0 and dic[K[0]] == dic[0]*2:
      print("Yes")
    else:
      print("No")
    exit()  
  if len(V) != 3:
    print("No")
    exit()
  if V[0] == V[1] and V[1] == V[2]:
    K = list(dic.keys())
    if K[0]^K[1] == K[2] and K[1]^K[2] == K[0] and K[2]^K[0] == K[1]:
      print("Yes")
    else:
      print("No")
  else:
    print("No")