a = list(map(int, input().split()))
t , u = a[0],a[1]

def c(x,y):
  if x % y:
    return(c(y,x%y))
  else:
    return(y)

print(c(t,u))
