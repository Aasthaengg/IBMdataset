n=int(input())
h=list(map(int,input().split()))
a=0 
c=0
for i in range(n):
 if c<h[i]:a+=h[i]-c
 c=h[i]
print(a)