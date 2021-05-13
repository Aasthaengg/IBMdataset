list_a_b = input().split()
list_a_b = [int(ll) for ll in list_a_b]
dd = list_a_b[0]*list_a_b[1]
if dd %2 ==0:
  print('Even')
else:
  print('Odd')