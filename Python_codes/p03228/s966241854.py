a,b,k = [int(i) for i in input().split()]

ct=1
for i in range(k):
  if ct==1:
    if a%2==0:
      b=b+a/2
      a=a/2
    else:
      b=b+(a-1)/2
      a=(a-1)/2
    ct=ct*-1
  else:
    if b%2==0:
      a=a+b/2
      b=b/2
    else:
      a=a+(b-1)/2
      b=(b-1)/2
    ct=ct*-1
print(int(a),int(b))