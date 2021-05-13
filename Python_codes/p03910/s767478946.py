import sys
N = int(input())
l = []

def main(n):
  global l
  i = 1
  while True:
    tmp = i*(i+1)//2
    if tmp >= n:
      l.append(i)
      if n-i == 0:
        return l
      else:
        return main(n-i)
    i += 1
    
sys.setrecursionlimit(10000)
li = main(N)
for n in li:
  print(n)