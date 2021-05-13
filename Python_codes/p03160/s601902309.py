n=int(input())
h=list(map(int, input().split()))

l=[0]*n
l[1]=abs(h[1]-h[0])

for i in range(2,n):
  if abs(h[i]-h[i-1])+l[i-1] >= abs(h[i]-h[i-2])+l[i-2]:
    l[i]=abs(h[i]-h[i-2])+l[i-2]
  else:
    l[i]=abs(h[i]-h[i-1])+l[i-1]
  #print(l)

print(l[-1])