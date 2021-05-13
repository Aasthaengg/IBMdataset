k = int(input())

neighbors = {'0': ['0', '1'], '1': ['0', '1', '2'], '2': ['1', '2', '3'], 
             '3': ['2', '3', '4'], '4': ['3', '4', '5'], '5': ['4', '5', '6'], 
             '6': ['5', '6', '7'], '7': ['6', '7', '8'], '8': ['7', '8', '9'], 
             '9': ['8', '9']}
queue = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
count = 0
#print(neighbors)
while True:
  num = queue.pop(0)
  count += 1
  if count == k:
    print(int(num))
    break
  else:
    num_last = num[-1]
    lst = neighbors[num_last]
    for ele in lst:
      num_add = num + ele
      queue.append(num_add)