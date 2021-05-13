N, P = map(int, input().split())
As = list(map(int, input().split()))
dic = {0:0, 1:0}
for a in As:
  if a % 2 == 0:
    dic[0] += 1
  else:
    dic[1] += 1

if P == 1 and dic[1] == 0:
  print(0)
  exit()
  
rlt = 2**dic[0]
tmp = 0
for i in range(dic[1]+1):
  if i == 0:
    t = 1
  else:
    t = t*(dic[1]+1-i)//i
  if (P == 0 and i%2==0) or (P == 1 and i%2==1):
    tmp += t
      
rlt *= tmp

print(rlt)