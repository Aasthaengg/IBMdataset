
H,W,A,B = map(int,input().split())
blk1 = [[0]*(W-A) for _ in range(H-B)]
blk2 = [[1]*(A) for _ in range(H-B)]
blk3 = [[1]*(W-A) for _ in range(B)]
blk4 = [[0]*(A) for _ in range(B)]

for i in range(len(blk2)):
    blk1[i]=blk1[i]+blk2[i]
#print(blk1)
  
for i in range(len(blk4)):
    blk3[i]=blk3[i]+blk4[i]

blk1 = blk1+blk3

#print(blk1)

for i in range(len(blk1)):
    print(''.join(str(x) for x in blk1[i]))

#print(blk3)