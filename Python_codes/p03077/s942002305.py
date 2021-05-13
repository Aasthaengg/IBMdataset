n= int(input())
b=10**15+1
for i in range(5):
    b=min(b,int(input()))
    
if n%b==0:
    print(4+n//b)
else:
    print(5+n//b)