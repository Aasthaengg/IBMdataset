n=int(input())
a=list(map(int,input().split()))
a_sorted=sorted(a,reverse=True)
diff=0
if n%2==0:
  for i in range(n//2):
    diff+=a_sorted[2*i]-a_sorted[2*i+1]
  print(diff)
else:
  for i in range(n//2):
    diff+=a_sorted[2*i]-a_sorted[2*i+1]
  print(diff+a_sorted[-1])