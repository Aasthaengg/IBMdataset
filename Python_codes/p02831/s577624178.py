A,B=map(int,input().split())

def larger(x,y):
  if x>y:
    return x
  else:
    return y

L=larger(A,B)
S=A+B-L

#rが最大公約数
r=L%S
while r!=0:
  L=S
  S=r
  r=L%S
  
#最小公倍数求める
p=(A*B)//S
print(p)