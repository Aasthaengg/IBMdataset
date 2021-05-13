import sys
sys.setrecursionlimit(10 ** 9)

n = int(input())
x = input()

p = [-1 for _ in range(2*(10**7)+1)]
cnt = x.count('1')

def calc(a):
  #print('a=',a)
  if 0 <= a <= 2*(10**7) and  p[a] != -1:
    return p[a]
  else:
    if a == 0:
      ret = 0
    else:
      b = bin(a).count('1')
      ret = 1+calc(a%b)
    if 0 <= a <= 2*(10**7):
      p[a] = ret
    return ret

if cnt > 1:
  x0 = int(x,2)%(cnt-1)
  xx0 = [1]
  for i in range(n+1):
    xx0.append((xx0[-1]*2)%(cnt-1))
x1 = int(x,2)%(cnt+1)
xx1 = [1]
for i in range(n+1):
  xx1.append((xx1[-1]*2)%(cnt+1))

y = list(x)  
for i in range(n):
  if y[i] == '0':
    xx = xx1[n-i-1]
    print(calc((x1+xx)%(cnt+1))+1)
  else:
    if cnt == 1:
      print(0)
    else:
      xx = xx0[n-i-1]
      print(calc((x0-xx)%(cnt-1))+1)