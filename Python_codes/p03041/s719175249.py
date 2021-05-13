n,k=[int(x) for x in input().rstrip().split()]
s=[i for i in input()]
ans=""
s[k-1]=s[k-1].lower()
for i in s:
  ans+=i
print(ans)