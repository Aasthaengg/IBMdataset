A,B=map(int,input().split())
total,outlet=0,1
while outlet<B:
  outlet = outlet-1
  outlet = outlet +A
  total = total+1
print(total)