a,b=map(int,input().split())
d=b-a

def A(n):
  hoge = int(n*(((n-1)/2)+1))
  return hoge

B=A(d)
print(B-b)