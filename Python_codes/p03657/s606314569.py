a,b = map(int, input().split())
ans='Possible'
if a%3!=0:
  if b%3!=0:
    if (a+b)%3!=0:
      ans='Impossible'
print(ans)