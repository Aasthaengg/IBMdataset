N = int(input())
HB = input().split(' ')
HB = [int(HB[i]) for i in range(N)]
Hs = [0]
for i in range(N):
  H = HB[i]
  if Hs[i] > H:
    print('No')
    break
  else:
   if Hs[i] == H:
     Hs.append(H)
   else:
     H = H - 1
     Hs.append(H)
else:
  print('Yes')