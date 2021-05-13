n=int(input())
a=list(map(int,input().split()))
cnt=1
for i in a:
    if i%2==0:
        cnt*=2
    
print(3**(len(a))-cnt)