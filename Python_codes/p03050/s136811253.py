import sys
readline=sys.stdin.buffer.readline

N=int(readline())

def make_divisors(n):
  divisors = []
  for i in range(1, int(n**0.5)+1):
    if n % i == 0:
      divisors.append(i)
      if i != n // i:
        divisors.append(n//i)
  return divisors

div=make_divisors(N)
#print(div)

answer=0
for i in range(len(div)):
  d=div[i]-1
  if d!=0 and N//d==N%d:
    answer+=d
print(answer)