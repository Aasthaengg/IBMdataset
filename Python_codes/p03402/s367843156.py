a,b=map(int,input().split())
h=100
w=100
g=h*w
A=[0 for i in range(g)]

a-=1
b-=1
ii=0
jj=0
for i in range(a):
   A[ii]=1
   ii+=2
   if i%(w//2)==w//2-1 :
       ii+=1+w
for i in range(b):
   A[-1*(jj+1)]=1
   jj+=2
   if i%(w//2)==w//2-1 :
       jj+=1+w

#print(A)
print("{} {}".format(h,w))
ans=""
for i in range(g):
    if i%w==0 and i!=0 :
        print(ans)
        ans=""
    
    if i>=g//2 :
        A[i]=(A[i]+1)%2
    if A[i]==1 :
        ans+="."
    else :
        ans+="#"

print(ans)
