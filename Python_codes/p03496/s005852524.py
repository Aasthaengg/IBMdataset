def p_xy(x,y):
  ansl.append(f"{x} {y}")

n=int(input())
a=list(map(int,input().split()))
mina=min(a)
maxa=max(a)
powa= maxa if abs(mina)<abs(maxa) else mina
powa_i=a.index(powa)
ansl=[]
if powa<0:
  for i in range(n):
    if a[i]>0:
      p_xy(powa_i+1,i+1)
  for i in reversed(range(1,n)):
      p_xy(i+1,i)
else:
  for i in range(n):
    if a[i]<0:
      p_xy(powa_i+1,i+1)
  for i in range(1,n):
    p_xy(i,i+1)
print(len(ansl))
print("\n".join(ansl))