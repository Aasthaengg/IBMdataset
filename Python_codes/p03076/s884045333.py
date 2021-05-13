def t(n):
  if n%10==0:
    return n
  else:
    return ((n//10)+1)*10
def k(n):
  if n%10==0:
    return 0
  else:
    return 10-(n%10)
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
L=[k(a),k(b),k(c),k(d),k(e)]
print(t(a)+t(b)+t(c)+t(d)+t(e)-max(L))