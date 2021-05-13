def p(x):
  return bin(x).count('1')

def f(x):
  if x == 0:
    return 0
  return f(x%p(x)) + 1

N = int(input())
X = input()
cnt = X.count('1')
x = int(X,2)
a = x % (cnt + 1)
if cnt != 1:
  b = x % (cnt - 1)

for i in range(N):
  if X[i] == '0':
    k = (a + pow(2,N-i-1,cnt+1))%(cnt+1)
  else:
    if cnt == 1:
      print(0)
      continue
    k = (b-pow(2,N-i-1,cnt-1))%(cnt-1)
  print(f(k)+1)