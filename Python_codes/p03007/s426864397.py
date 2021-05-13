n=int(input())
a=list(map(int,input().split()))
plus=[a[i] for i in range(n) if a[i]>=0]
l_plus=len(plus)
minus=[a[i] for i in range(n) if a[i]<0]
l_minus=len(minus)
x_cal=[]
y_cal=[]
if n==2:
  a.sort()
  print(a[1]-a[0])
  print(a[0],a[1])
else:
  if plus!=[] and minus!=[]:
    if l_plus>1:
      x_cal.append(minus[0])
    for j in range(1,l_plus-1):
      x_cal.append(x_cal[-1]-plus[j])
    for k in range(1,l_plus):
      y_cal.append(plus[k])
    if l_plus>1:
      y_last=x_cal[-1]-y_cal[-1]
    else:
      y_last=minus[0]
    x_cal.append(plus[0])
    for j in range(1,l_minus):
      x_cal.append(x_cal[-1]-minus[j])
    for k in range(1,l_minus):
      y_cal.append(minus[k])
    y_cal.append(y_last)
    print(x_cal[-1]-y_cal[-1])
    for ii in range(n-1):
      print(x_cal[ii],y_cal[ii])
  elif minus==[]:
    a.sort()
    print(sum(a)-2*a[0])
    x_cal.append(a[0])
    for ij in range(1,n-2):
      x_cal.append(x_cal[-1]-a[ij])
    for jj in range(0,n-2):
      y_cal.append(a[jj+1])
    y_cal.append(x_cal[-1]-y_cal[-1])
    x_cal.append(a[-1])
    for ii in range(n-1):
      print(x_cal[ii],y_cal[ii])
  else:
    a.sort()
    print(a[-1]*2-sum(a))
    x_cal.append(a[-1])
    for ij in range(1,n-2):
      x_cal.append(x_cal[-1]-a[ij])
    for jj in range(0,n-2):
      y_cal.append(a[jj+1])
    x_cal.append(x_cal[-1]-y_cal[-1])
    y_cal.append(a[0])
    for ii in range(n-1):
      print(x_cal[ii],y_cal[ii])