N=int(input())
a=100000
for i in range(N):
    x=a+(a*0.05)
    
    if x%1000==0:
        a=x
    else:
        a=(x-(x%1000))+1000

print(int(a))
