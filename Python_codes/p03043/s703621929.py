n,k=map(int,input().split())
a=0
for i in range(n):
 x=i+1;y=0
 while x<k:x*=2;y+=1
 a+=1/2**y
print(a/n)