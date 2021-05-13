def main():
  n = int(input())
  l = []
  a,b = 0,1
  for x in range(n+1):
    if x%15==0:
      pass
     # l.append('FizzBuzz')
    elif x%5==0:
      pass
     # l.append('Buzz')
    elif x%3==0:
      pass
     # l.append('Fizz')
    else:
      l.append(x)
      
  print(sum(l))    


if __name__ == '__main__':
  main()