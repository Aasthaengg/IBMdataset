n,k=map(int,input().split())
s=input()

if n==1:
  print(s.lower())
elif k==1:
  print(s[0].lower()+s[1:])
elif k==n:
  print(s[:n-1]+s[n-1].lower())
else:
  print(s[:k-1]+s[k-1].lower()+s[k:])