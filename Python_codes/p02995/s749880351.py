import math

def Div(a,b,c):
  #a<=x<=bのうちcで割り切れるものの数を返す
  l = ((a-1)//c+1)*c
  r = (b//c)*c
  return (r-l)//c+1

A,B,C,D = map(int,input().split())

print(B-A+1-(Div(A,B,C)+Div(A,B,D)-Div(A,B,C*D//math.gcd(C,D))))