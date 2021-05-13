a,b,x=map(int,input().split())

def f_mod(a,x):
  return a//x+1

print(f_mod(b,x)-f_mod(a-1,x))