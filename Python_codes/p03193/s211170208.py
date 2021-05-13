inputs=lambda:map(int,input().split())
cnt=0
n,h,w=inputs()
for i in range(n):
  a,b=inputs()
  if a>=h and b>=w:
    cnt+=1
    
print(cnt)