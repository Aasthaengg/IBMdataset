N=int(input())
*H,=map(int,input().split())

for i in range(-1,-len(H),-1):
   #print(i,H[i],H[i-1])
   if H[i]<H[i-1]-1:
    print('No')
    break
   if H[i-1]-1 == H[i]:
    H[i-1]=H[i]
else:
   print('Yes')