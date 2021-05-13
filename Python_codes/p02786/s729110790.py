h=int(input())
def f(x):
  if x==1:
    return 1
  return f(x//2)*2

ans=f(h)
print(ans*2-1)