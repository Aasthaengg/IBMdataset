n = int(input())

f = n//3
b = n//5
fb = n//15

def s(x):
  return x*(x+1)/2

ans = s(n) - 3*s(f) - 5*s(b) + 15*s(fb)
print(int(ans))