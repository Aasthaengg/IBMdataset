a, b, c, d = map(int, input().split())

def ans(a,b,c,d):
  while 1:
    c -= b
    if c <= 0:
      return("Yes")
    a -= d
    if a <= 0:
      return("No")

print(ans(a,b,c,d))
