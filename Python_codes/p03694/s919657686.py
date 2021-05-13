a=int(input())
b=list(map(int,input().split()))
 
b=sorted(b)
sum=0
 
for i in range(1,a):
    sum+=b[i]-b[i-1]
 
print(sum)