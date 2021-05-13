
def f(H):
  return 2*f(H//2)+1 if H>1 else 1

H=int(input())
print(f(H))
