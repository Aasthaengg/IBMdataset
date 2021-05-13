n=int(input())
for i in range(n+7):
  if i*(i+1)//2>=n:w=i;break
for i in range(w,0,-1):
  if n>=i:
    print(i)
    n-=i