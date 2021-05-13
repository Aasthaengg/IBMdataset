n, h, w= [int(i) for i in input().split()]
e = [[int(i) for i in input().split()] for i in range(n)] 
#print(n,h,w)
#print(e)
cnt=0
for j in range(n):
  if e[j][0]>=h and e[j][1]>=w:
    cnt+=1
print(cnt)