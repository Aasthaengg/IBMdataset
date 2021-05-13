def KiriageTime(x):
  return (x+9)//10*10

def sabun(x):
  return KiriageTime(x)-x

A=int(input())
B=int(input())
C=int(input())
D=int(input())
E=int(input())
KiriageTotal=KiriageTime(A)+KiriageTime(B)+KiriageTime(C)+KiriageTime(D)+KiriageTime(E)
print(KiriageTotal-max(sabun(A),sabun(B),sabun(C),sabun(D),sabun(E)))
