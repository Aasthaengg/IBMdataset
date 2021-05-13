N = input()
A = list(input().split())
A = list(map(int,A))
A = sorted(A,reverse = True)
a = 0
b = 0
try :
  while len(A) != 0 :
    a += A.pop(0)
    b += A.pop(0)
  print(a-b)
except IndexError :
  print(a-b)

