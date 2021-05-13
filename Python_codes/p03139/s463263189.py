n,a,b = map(int,input().split())
max1 = min(a,b)
if a+b <= n:
  min1 =0
elif a+b >n:
  min1 = a+b-n
print(max1,min1)