a,b=input().split()
print(['<','=','>'][min(2,max(0,1+int(a,16)-int(b,16)))])