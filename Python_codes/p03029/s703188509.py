def solver():
    A, P = [int(n) for n in input().split()]
    return (A*3+P)//2

if __name__=='__main__':
  print(solver())
