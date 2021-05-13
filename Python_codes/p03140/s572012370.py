N = int(input())
A = input()
B = input()
C = input()

ret = 0
for i in range(N) :
  s = set([A[i], B[i], C[i]])
  if len(s) == 3 :
    ret += 2
  elif len(s) == 2 :
    ret += 1
  
print(ret)