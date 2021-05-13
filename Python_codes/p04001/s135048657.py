import copy
a = list(input())
N=len(a)
bit_list =[]
for i in range(2**(N-1)):
  b = format(i,"09b")
  b = b[::-1]
  bit_list.append(b)
count = 0
for i in range(2**(N-1)):
  a_list = []
  a_list=copy.copy(a)
  num = 0
  num_li =[a[0]]
  for k,j in enumerate(bit_list[i]):
    if j == '1':
      a_list.insert(k+1+num,"+")
      num+=1
  for j,i in enumerate(a_list):
    if j>0:
      num_li[0] +=i
  count+= eval(num_li[0])
print(count)