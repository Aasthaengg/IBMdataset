str1 ='abcdefghijklmnopqrstuvwxyz'
N = input()
count = 0
for i in str1:
  if i not in N:
    print(i)
    count +=1
    break
if count ==0:
  print('None')