import math

def calc(A, B) : 
  a = math.log(A)
  b = math.log(B)
  if a > b : 
    print('GREATER')
  elif b > a : 
    print('LESS')
  else : 
    print('EQUAL')
    
A = int(input())
B = int(input())

calc(A, B)