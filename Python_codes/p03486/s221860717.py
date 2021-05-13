s=sorted(input())
t=sorted(input(), reverse=True)
ans='No'
if s<t:
  ans='Yes'
print(ans)