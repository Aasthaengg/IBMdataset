def main(h):
  count = 1
  n = 0
  for i in range (k):
    n = (n * 10 + 7) % k  
    if n == 0: 
      print(count)
      return 0
    count += 1
  print(-1)
  
if __name__ == '__main__':
  k = int(input())
  main(k)