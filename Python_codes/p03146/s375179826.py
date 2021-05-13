s = int(input())

seq = [s]

def f(n):
  if n % 2 == 0:
    return n //2
  else:
    return 3 * n + 1

m = 1
while True:
  i = m-1
  a = f(seq[i])
  
  if a in seq:
    break
  seq.append(a)
  m += 1
print(m+1)