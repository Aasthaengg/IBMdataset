NN = input()
AA = int(NN[0:2])
BB = int(NN[2:])

count1 = 0
count2 = 0
if AA > 12 or AA == 00:
  count1 +=1
if BB > 12 or BB == 00:
  count2 +=1
if count1 == 0 and count2 == 0:
  print('AMBIGUOUS')
elif count1 ==1 and count2 == 0:
  print('YYMM')
elif count1 ==0 and count2 == 1:
  print('MMYY')
else:
  print('NA')