n,h,w=map(int,input().split())
cnt=0
for i in range(n):
  hh,ww=map(int,input().split())
  if hh>=h and ww>=w:
    cnt+=1
    
print(cnt)