a,b,c=map(int,input().split())
s=set()
i=1
while True:
  x=a*i%b
  if x in s:
    break
  s.add(x)
  i+=1
ans = "YES" if c in s else "NO"
print(ans)