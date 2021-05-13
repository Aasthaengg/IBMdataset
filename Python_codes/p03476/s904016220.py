import math

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

sosuu=[]
for i in range(1,10**5,2):
  if is_prime(i):
    if is_prime((i+1)//2):
      sosuu.append(i)
sosuu1=[0]*(10**5+1)
for i in range(2,10**5):
  sosuu1[i]=sosuu1[i-1]
  if i in sosuu:
    sosuu1[i]+=1
N = int(input())
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]
for i in range(N):
  print(sosuu1[y[i]]-sosuu1[x[i]-2])