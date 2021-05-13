A,B,C = map(int, input().split())
n = 0
while A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
  if A == B == C:
    print ('-1')
    exit()
  else:
    a = B/2 + C/2
    b = A/2 + C/2
    c = A/2 + B/2
    A = a
    B = b
    C = c
    n += 1
  
  
print(n)