N=int(input())
def f(n):
  n=str(n)
  if n[0]==n[1]==n[2]:
    return True
  else:
    return False

for i in range(N,1000):
  if f(i):
    print(i)
    exit(0)