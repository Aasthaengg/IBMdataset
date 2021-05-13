a,b,c=map(int,input().split())

ans='No'

if a==b:
  if b!=c:
    ans='Yes'
elif b==c:
  ans='Yes'
elif a==c:
  ans='Yes'

print(ans)