N=int(input())
count=0
for i in range(1,N+1):
    a=str(i)
    b=len(a)
    if b%2!=0:
        count+=1
    else:
        count+=0
print(count)