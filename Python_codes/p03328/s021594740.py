sumA=0
diff={}
for i in range(1,1000):
  sumA+=i
  diff[i]=sumA
#print(diff)
a,b=[int(i) for i in input().split()]
print(diff[b-a]-b)