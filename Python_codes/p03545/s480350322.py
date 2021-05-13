def main():
  s = input()

  for op in range(16):
    t = s[0]
    for j in range(3):
      if (op & (1 << j)):
        t = t + "+"
      else:
        t = t + "-"
      t = t + s[j+1]
    #print(op,t,eval(t))
    if eval(t) == 7:
      print(t + "=7")
      exit(0)
      
  
if __name__ == '__main__':
  main()