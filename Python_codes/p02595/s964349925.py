def counter(arr, d):
  import math
  count = 0
  for item in arr:
    a = int(item[0])
    b = int(item[1])
    lenght = math.sqrt(a**2+b**2)
    #print(lenght)
    if lenght <= d:
      count += 1
  print(count)  
      

if __name__ == '__main__':
  line1 = input().split(" ")
  d = int(line1[1])
  num = int(line1[0])
  #print(d, num)
  arr = []
  for i in range(num):
    line = input().split(" ")
    arr.append(line)
  counter(arr, d)