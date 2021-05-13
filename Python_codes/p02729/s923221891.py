n,m=map(int,input().split())
def num(x):
  if x<2:
    return 0
  else:
    return int(x*(x-1)/2)
print(num(n)+num(m))