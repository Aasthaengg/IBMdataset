n = int(input())
a= [int(i) for i in input().split()]

for i in range(len(a)):
    a[i]-=i+1

aa=sorted(a)
if n%2==0:
  b=(aa[int(n/2-1)]+aa[int(n/2)])/2
else:
  b=aa[int((n-1)/2)]

s=0
for i in aa:
  s+=abs(i-b)
print(int(s))

