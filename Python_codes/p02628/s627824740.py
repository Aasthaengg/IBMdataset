def main():
  n,k = list(map(int, input().split()))
  p = list(map(int, input().split()))
  p.sort()
  p2 = p[:k]
  print(sum(p2))
    
    
    
 
if __name__ == '__main__':
  main()