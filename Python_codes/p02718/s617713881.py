a,b = map(int, input().split())
c = list(map(int,input().split()))

d = sum(c)
e = sorted(c,reverse=True)

for i in range(b):
  if(e[i]<d/(4*b)):
    print("No")
    exit()
print("Yes")