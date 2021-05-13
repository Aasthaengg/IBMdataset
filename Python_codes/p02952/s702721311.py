N=int(input())
a=0
for i in range(N,0,-1):
    l=len(str(i))
    if l%2!=0:
        a+=1
print(a)