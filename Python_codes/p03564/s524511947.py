n=int(input())
k=int(input())
a=1
b=0
while k>a and b<n:
    a=a*2
    b+=1
for i in range(n-b):
    a+=k
print(a)