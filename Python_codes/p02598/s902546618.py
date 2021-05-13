from math import ceil
n, k = map(int, input().split())
a = list(map(int, input().split()))
mi = 0
ma = max(a)
m = ma//2
while ma-mi>1:
  temp = 0
  for i in range(n):
    temp += ceil(a[i]/m)-1 
    #if a[i]%m==0:
    #  temp-=1
  if temp<=k:
    ma=m
    m=(ma+mi)//2
  else:
    mi = m
    m=(ma+mi)//2
  #print("temp " + str(temp))
  #print("ma " + str(ma)+ " mi " + str(mi) + " m " + str(m))
#print(m)
print(m+1)