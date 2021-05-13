c=[0 for i in range(10000)]

for x in range(1,101):
  for y in range(1,101):
    for z in range(1,101):
      n=x*x+y*y+z*z+z*y+y*x+x*z
      if n<=10000:
        c[n-1]+=1
print("\n".join(list(map(str,c))[:int(input())]))
