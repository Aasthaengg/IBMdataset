n,k=map(int,input().split())
a=0
for i in range(1,n+1):
    j=0
    while i<k:
        i*=2
        j+=1
    a+=0.5**j
print(a/n)