N=int(input())
*H,=map(int,input().split())

i=c=a=0
while i<N-1:
 if 1<=H[i]/H[i+1]:c+=1
 else:
   a=max(a,c)
   c=0
 i+=1
print(max(a,c))