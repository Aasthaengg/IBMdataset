a,b,c = map(int,input().split(" "))
count = 0
for i in range(a):
  d,e = map(int,input().split(" "))
  if d >= b and e >= c:
    count += 1
print(count)