def waru(A,B):
  if A%B==0:
    return A//B
  else:
    return (A//B)+1
N=int(input())
A=int(input())
B=int(input())
C=int(input())
D=int(input())
E=int(input())
a=min([A,B,C,D,E])
print(waru(N,a)+4)