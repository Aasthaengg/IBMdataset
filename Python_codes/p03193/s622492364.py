n,h,w=map(int, input().split())
c=0
for i in range(n):
  A,B=map(int, input().split())
  if A>=h and B>=w:
    c+=1
print(c)