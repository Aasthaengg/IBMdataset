n=int(input())
a=list(map(int,input().split()))
s=[0]*n
diff=[0]*(n)
Sum=0
for i in range(n):
  Sum+=a[i]
  s[i]=Sum
#print(s)
SUM=sum(a)
for i in range(n):
  diff[i]=abs(s[i]-(SUM-s[i]))
  
#print(diff)
print(min(diff))