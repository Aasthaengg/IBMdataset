H = input().split()
sdy =0
if int(H[2]) >= int(H[0]):
  sdy = int(H[2])*60 +int(H[3])-int(H[0])*60 -int(H[1]) - int(H[4])
else:
  H[2] = (int(H[2])+24)
  sdy = int(H[2])*60 +int(H[3])-int(H[0])*60 -int(H[1]) - int(H[4])
if int(sdy) < 0:
  sdy = 0
print(sdy)