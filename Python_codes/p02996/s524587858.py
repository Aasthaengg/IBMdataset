import sys
n=int(input())
ab=[]
for i in range(n):
  AB=[int(x) for x in input().rstrip().split()]
  ab.append(AB)
# ab=sorted(ab,key=lambda x :x[0])
ab=sorted(ab,key=lambda x :x[1])

time=0
for a,b in ab:
  if time+a<=b:
    time+=a
  else:
    print("No")
    sys.exit()

print("Yes")