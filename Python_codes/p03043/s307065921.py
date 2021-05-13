n,k=map(int,input().split())
cnt=0
j=17
for i in range(1,n+1):
    if i>=k:
        cnt+=1
    else:
        while i*(2**j)>=k:
            j-=1
        cnt+=1/2**(j+1)
print(format(cnt/n,'.12f'))
