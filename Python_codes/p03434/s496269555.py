input();a,b,c=0,0,sorted(map(int,input().split()))
while c:
  a+=c.pop()
  b+=c.pop() if c else 0
print(a-b)