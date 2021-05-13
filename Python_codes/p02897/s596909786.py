s=0
t=0
n=int(input())
for x in range(1,n+1):
    if x%2==1:
        s+=1
print(s/n)