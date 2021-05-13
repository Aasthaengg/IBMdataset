n,m=map(int,input().split())


result=[]
if m%2==1:
    j=1
    for i in range(m//2):
        result.append((j,2*(m//2-i)+j))
        j+=1
    j=2*(m//2)+2
    for i in range(m//2+1):
        result.append((j,2*(m//2+1-i)+j-1))
        j+=1

else:
    j=1
    for i in range(m//2):
        result.append((j,2*(m//2-i)+j))
        j+=1
    j=2*(m//2)+2
    for i in range(m//2):
        result.append((j,2*(m//2-i)+j-1))
        j+=1

    
for item in result:
    print(item[0],item[1])
