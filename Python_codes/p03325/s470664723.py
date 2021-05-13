N=int(input())
a=list(map(int,input().split()))

def f(n):
  count = 0
  while 1:
    if n % 2 == 0:
      n //= 2
      count += 1
    else:
      return count

print(sum(map(f,a)))