n=int(input())
s=input()
if len(s)%2==1:
  print ('No')
else:
  k=s[:n//2]
  if k+k==s:
    print ('Yes')
  else:
    print ('No')