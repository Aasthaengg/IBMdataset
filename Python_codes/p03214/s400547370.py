n =int(input())
a=[int(x) for x in input().split()]
 
s=sum(a)
ans=0
diff=abs(s-a[0]*n)
for i in range(n):
  if diff>abs(s-a[i]*n): 
    diff= abs(s-a[i]*n)
    ans=i
print(ans)