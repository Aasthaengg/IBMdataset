a,b,k=map(int,input().split())

while k>0:
  if a%2==0:
    b+=a/2
    a-=a/2
  else:
    a-=1
    b+=a/2
    a-=a/2
  
  k-=1
  if k==0:
    break
    
  if b%2==0:
    a+=b/2
    b-=b/2
  else:
    b-=1
    a+=b/2
    b-=b/2
    
  k-=1
  
print(int(a),int(b))