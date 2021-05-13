def main():
  n =int(input())
  li = [0] * n
  
  for i in range(1, n+1):
    li[i-1] += i
  
  length = len(li)
  total = 0
  
  for k in range(0, length):
    if li[k] % 3 != 0 and li[k] % 5 != 0:
      total += li[k]
      
  print(total)
      
  
main()
