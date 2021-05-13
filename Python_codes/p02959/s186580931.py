n=int(input())
a=list(map(int,input().split()))#モンスター数
b=list(map(int,input().split()))#勇者キャパ
sm=0
c=0
for i in range(n):
  if c >=a[i]:
    sm+=a[i]
    c=b[i]
  elif b[i]+c>=a[i]:
    sm+=a[i]
    c=-a[i]+c+b[i]
  else:
    sm+=b[i]+c
    c=0
sm+=min(c,a[-1])
print(sm)
  
