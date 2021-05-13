n=int(input())

ans=[]
if(n==0):
    print(0)
    exit()


while n!=0:
    r=n%2
    ans.append(r)
    n=int((n-r)/(-2))

ans.reverse()

for i in ans:
    print(i,end='')

