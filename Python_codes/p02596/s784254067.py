k = int(input())
d1 = k % 10
mae = 0
sd = [0]*10
cnt = 0
if not d1 in (1, 3, 7, 9):
  print(-1)
  exit()
for i in range(1,10) :
  sd[d1 * i % 10] = i
#print(sd)

for j in range(999999):
  d2 = 7 - mae % 10
  s = str(sd[d2] * k + mae)
#  print("mae ", mae,"",sd[d2] * k )
#  print("s1=",s)
  for i in range(len(s)-1, -1, -1):
#    print("s[",i,"]=",s[i])
    if (s[i]) == "7":
      cnt += 1
    else:
      s = s[0:i+1]
      mae = int(s)
#      print("s2=",s)
      break
#    print("i= ",i)
    if i == 0 :
      print(cnt)
      exit()