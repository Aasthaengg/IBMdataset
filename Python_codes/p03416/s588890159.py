A,B=map(int,input().split())
N = 0
res = 0
def checkPali(n):
  # n = 100*a + 10*b +c
  c = n%10
  a = n//10000
  b = (n - 10000*a)//1000
  d = (n - c)/10
  e = d%10
  if a == c and b == e:
    return True
  else:
    return False
for i in range(B-A+1):
  N = A + i
  if checkPali(N):
    res+=1
print(res)