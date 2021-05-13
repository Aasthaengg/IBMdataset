import sys
a,b,c,d = input()
a,b,c,d = int(a),int(b),int(c),int(d)
op=["-","+"]
for i in op:
  for j in op:
    for k in op:
      if i=="-":
        now=a-b
      else:
        now=a+b
      
      if j=="-":
        now=now-c
      else:
        now=now+c
      
      if k=="-":
        now=now-d
      else:
        now=now+d
      
      if now==7:
        print(str(a)+i+str(b)+j+str(c)+k+str(d)+"="+"7")
        sys.exit()
      else:
        now=0