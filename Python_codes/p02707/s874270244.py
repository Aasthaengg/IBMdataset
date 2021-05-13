def main():
  a = int(input())
  b =[0]*a
  
  for c in map(int, input().split()):
    b[c-1] += 1
    
  print('\n'.join(map(str, b)))
 
main()