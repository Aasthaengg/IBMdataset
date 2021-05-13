n,m=map(int,input().split())
sc=[list(map(int,input().split())) for i in range(m)]

for i in range(1000):
  num_str = str(i)
  num_keta = len(num_str)
  
  if num_keta != n:
    continue
    
  flg = True
  for j in range(m):
    pos = sc[j][0] - 1
    val_str = str(sc[j][1])
    if num_str[pos] != val_str:
      flg = False

  if flg:
    print(num_str)
    exit(0)
print('-1')
