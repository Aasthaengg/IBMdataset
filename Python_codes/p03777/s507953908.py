a,b=input().split()
def ch(x):
  return 1 if x=="D" else -1
a=ch(a)
b=ch(b)
print("H" if a*b==1 else "D")