k=int(input())
a,b=map(int,input().split())
if k==1 or a%k==0 or b%k==0 or(b-a)+(a%k)>=k:
  print("OK")
else:
  print("NG")